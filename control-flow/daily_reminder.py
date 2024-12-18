task = input("Enter task description: ")
priority = input("Enter task priority (high, medium, low): ")
time_bound = input("Is the task is time-bound (yes or no): ")
match time_bound:
    case "yes":
        print(f"Reminder: {task} is a {priority} priority task that requires immediate attention today!")
    case _ if "no":
        print(f"Note: {task} is a {priority} priority task. Consider completing it when you have free time.")
   