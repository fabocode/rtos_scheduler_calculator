#  RTOS Scheduler Calculator 
A set of python programs that should help with the analysis of feasibility for RTOS Schedulers

# What you can calculate
- Largest possible frame to to use in Cyclic Structured Scheduler

# Usage
- At the moment, it's just a terminal based program which is going to ask you for the number of tasks you want to run and is going to ask for the Period, Execution time and Deadline, all of this is measured in milliseconds (ms)

# Cyclic Structured Scheduler Largest Possible Frame Example
You receive a set of tasks with the following details 
- Task 1 
  - Period: 5
  - Execution time: 1
  - Deadline: None (if there is no deadline provided, the assummed deadline is the Period of the task)
- Task 2
  - Period: 7
  - Execution time: 2
  - Deadline: None
- Task 3
  - Period: 8
  - Execution time: 3
  - Deadline: None

The output is going to be the following: 


```terminal
rtos_scheduler_calculator\cyclic_structured_scheduler> python .\main.py
Find the largest possible frame size for the cyclic structured scheduler
Enter the number of tasks: 3
---------- Enter details for Task (T1)-----------------
Enter the period: 5
Enter the execution time: 1
Does the task have a deadline? (y/n): n

---------- Enter details for Task (T2)-----------------
Enter the period: 7
Enter the execution time: 2
Does the task have a deadline? (y/n): n

---------- Enter details for Task (T3)-----------------
Enter the period: 8
Enter the execution time: 3
Does the task have a deadline? (y/n): n

Task (T1) : Period: 5, Execution Time: 1.0, Deadline: 5
Task (T2) : Period: 7, Execution Time: 2.0, Deadline: 7
Task (T3) : Period: 8, Execution Time: 3.0, Deadline: 8

Candidate frames:  [8, 7, 5, 4, 2, 1]
Largest frame size possible:  2
The largest frame size does not satisfy the requirement f (2) >= max_execution_time (3.0)
That could mean that the task with the largest execution time will must split into parts to fit into the frame
```