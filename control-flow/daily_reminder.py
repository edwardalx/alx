task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? ")
match time_bound:
    case "yes":
        print(f"Reminder: {task} is a {priority} priority task that requires immediate attention today!")
    case _ if "no":
        print(f"Note: {task} is a {priority} priority task. Consider completing it when you have free time.")
   