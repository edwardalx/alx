Task = input("Enter task description: ")
Priority = input("Enter task priority (high, medium, low): ")
Time_bound = input("Is the task is time-bound (yes or no): ")
match Time_bound:
    case "yes":
        print(f"Reminder: {Task} is a {Priority} priority task that requires immediate attention today!")
    case _ if "no":
        print(f"Note: {Task} is a {Priority} priority task. Consider completing it when you have free time.")
   