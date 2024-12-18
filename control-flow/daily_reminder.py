task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
while priority.lower() not in ["high","medium","low"]:
    priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
while time_bound.lower() not in ["yes", "no"]:
    time_bound = input("Is it time-bound? (yes/no): ")
match priority:
    case "high":
          message = f"'{task}' is {priority} priority task "
    case "medium":
          message = f"'{task}' is {priority} priority task "
    case "low":
          message = f"'{task}' is {priority} priority task "
          
if  time_bound == "yes":
    
    print(f"Reminder:{message} that requires immediate attention today!")         
else:
    print(f"Note:{message}. Consider completing it when you have free time.")         
   