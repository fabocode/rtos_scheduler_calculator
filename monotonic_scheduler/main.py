'''
Calculate the system's utilization factor

Schedulability test

for example, a system with the task set
T1 (5, 1, 5)
T2 (4, 0.5, 4)
T3 (6, 1.2, 6)

Total Utilization (U) = 1/5 + 0.5/4 + 1.2/6 = 0.525 and 

urm (3) = 3(2^(1/3) - 1) = 0.7798

Since U < urm (3), the system is schedulable. (guaranteed feasible)

The total utilization equation is derived from the following equation:

U = total sum of (ei/pi)

and urm could be calculated as follows:

Urm(n) = n(2^(1/n) - 1)
where n is the number of the tasks

then you need to verify that 
U <= Urm and if this condition is true, the system is guaranteed feasible
'''

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

def get_total_utilization(tasks):
    print("---------- Total Utilization (U) -----------------")
    total_utilization = 0
    for task in tasks:
        print("execution_time/period -> {}/ {}".format(task["execution_time"], task["period"]))
        total_utilization += task["execution_time"] / task["period"]
    return total_utilization

def get_urm(num_tasks):
    return num_tasks * (2 ** (1/num_tasks) - 1)

def read_tasks():
     # Get the number of tasks
    num_tasks = int(input("Enter the number of tasks: "))
    if num_tasks <= 0:
        print("Invalid number of tasks")
        return

    if num_tasks == 1:
        print("Only one task. The frame size is the period of the task")
        return

    task_dict = {}
    # periods = [] 
    # max_exec_time = 0
    # Get the task details
    for i in range(num_tasks):
        task_id = i+1
        print("---------- Enter details for Task (T%d)-----------------" % (task_id))
        period = int(input("Enter the period: "))
        # periods.append(period)
        execution_time = float(input("Enter the execution time: "))
        has_deadline = input("Does the task have a deadline? (y/n): ")
        if has_deadline.lower() == 'y':
            deadline = int(input("Enter the deadline: "))
        else:
            deadline = period
        task_dict[task_id] = Task(task_id, period, execution_time, deadline)

        # save the max execution time
        # if execution_time > max_exec_time:
        #     max_exec_time = execution_time
        # print("")

    # Print all the tasks
    print("")
    print("----------------- Tasks -----------------")
    for i in range(num_tasks):
        task_id = i+1
        task = task_dict[task_id]
        print("Task (T{}) : Period: {}, Execution Time: {}, Deadline: {}".format(task.task_id, task.period, task.execution_time, task.deadline))
    print("")

    # return task_dict, periods, max_exec_time
    return task_dict

def main():
    """
        Calculate the system's utilization factor
    """
    # task_dict, periods, max_exec_time = read_tasks()
    task_dict = read_tasks()
    tasks = [task.get_details() for task in task_dict.values()] # Convert the task objects to a list of dictionaries
    total_utilization = get_total_utilization(tasks)
    urm = get_urm(len(task_dict))
    print("")
    print("---------- Results -----------------")
    print("Total Utilization = \t{}".format(total_utilization))
    print("Urm = \t{}".format(urm))
    print("")
    print("total utilization {} <= {} urm".format(total_utilization, urm))
    print("")
    print("----------------- Conclusion -----------------")
    if total_utilization <= urm:
        print("The system is guaranteed feasible")
    else:
        print("The system is NOT guaranteed feasible")

        if urm < total_utilization < 1:
            print("")
            print("but wait...")
            print("urm {} < {} total_utilization < 1".format(urm, total_utilization))
            print("since U > urm but less than 1, neither")
            print("feasibility nor overloading can be guaranteed")
            print("more tests must be applied to verify whether it is feasible")

if __name__ == "__main__":
    main()
