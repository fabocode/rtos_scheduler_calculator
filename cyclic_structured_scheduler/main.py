from math import gcd

def get_LCM(periods):
    lcm = 1
    for i in periods:
        lcm = lcm*i//gcd(lcm, i)
    return lcm

def find_valid_candidates(periods):
    hyperperiod = get_LCM(periods)  # Calculate the hyperperiod
    
    largest_period = max(periods)
    valid_candidates = []
    
    candidate_period = largest_period
    while candidate_period >= 1:
        if hyperperiod % candidate_period == 0:
            valid_candidates.append(candidate_period)
        candidate_period -= 1
    
    return valid_candidates

def evaluate_condition(frame_size, tasks):
    for task in tasks:
        period = task["period"]
        deadline = task["deadline"]
        
        if (2 * frame_size - gcd(period, frame_size)) > deadline:
            return False  # The condition doesn't hold for this frame size
    return True

def find_optimal_frame_size(frame_candidates, tasks):
    for frame_size in frame_candidates:
        if evaluate_condition(frame_size, tasks):
            return frame_size
    return None  # No suitable frame size found

class Task:
    def __init__(self, task_id, period, execution_time, deadline=None):
        self.task_id = task_id
        self.period = period
        self.execution_time = execution_time
        if deadline is None:
            self.deadline = period
        else:
            self.deadline = deadline

    def get_period(self):
        return self.period
    
    def get_execution_time(self):
        return self.execution_time

    def get_deadline(self):
        return self.deadline
    
    def get_details(self):
        return {
            "task_id": self.task_id, 
            "period": self.period, 
            "execution_time": self.execution_time, 
            "deadline": self.deadline
            }

def main():
    print("Find the largest possible frame size for the cyclic structured scheduler")
    
    # Get the number of tasks
    num_tasks = int(input("Enter the number of tasks: "))

    task_dict = {}
    periods = [] 
    max_exec_time = 0
    # Get the task details
    for i in range(num_tasks):
        task_id = i+1
        print("---------- Enter details for Task (T%d)-----------------" % (task_id))
        period = int(input("Enter the period: "))
        periods.append(period)
        execution_time = float(input("Enter the execution time: "))
        has_deadline = input("Does the task have a deadline? (y/n): ")
        if has_deadline.lower() == 'y':
            deadline = int(input("Enter the deadline: "))
        else:
            deadline = period
        task_dict[task_id] = Task(task_id, period, execution_time, deadline)

        # save the max execution time
        if execution_time > max_exec_time:
            max_exec_time = execution_time
        print("")

    # Print all the tasks
    for i in range(num_tasks):
        task_id = i+1
        task = task_dict[task_id]
        print("Task (T{}) : Period: {}, Execution Time: {}, Deadline: {}".format(task.task_id, task.period, task.execution_time, task.deadline))
    print("")
    
    # requirement 2: candidates divide H evenly (H is the hyper period) and the candidates are all the possible frame sizes
    frame_candidate_list = find_valid_candidates(periods)
    print("Candidate frames: ", frame_candidate_list)

    # requirement 3: choose the largest candidate frame size
    tasks = [task.get_details() for task in task_dict.values()] # Convert the task objects to a list of dictionaries
    largest_frame_size = find_optimal_frame_size(frame_candidate_list, tasks)

    if largest_frame_size is None:
        print("No suitable frame size found")
    else:
        print("Largest frame size possible: ", largest_frame_size)

        # The requirement 1 says that the frame size should be greater than or equal to the largest execution time
        # f >= max_execution_time
        if largest_frame_size >= max_exec_time:
            print("The largest frame size satisfies the requirement f ({}) >= max_execution_time ({})".format(largest_frame_size, max_exec_time))
        else:
            print("The largest frame size does not satisfy the requirement f ({}) >= max_execution_time ({})".format(largest_frame_size, max_exec_time))
            print("That could mean that the task with the largest execution time will must split into parts to fit into the frame")
        
if  __name__ == "__main__":
    main()
