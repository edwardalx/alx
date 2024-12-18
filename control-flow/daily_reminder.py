task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
while priority.lower() not in ["high","medium","low"]:
    priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
while time_bound.lower() not in ["yes", "no"]:
    time_bound = input("Is it time-bound? (yes/no): ")
match time_bound.lower():
    case "yes":
        print(f"Reminder: {task} is a {priority} priority task that requires immediate attention today!")
    case _ if "no":
        print(f"Note: {task} is a {priority} priority task. Consider completing it when you have free time.")
   