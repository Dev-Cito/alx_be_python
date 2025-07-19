
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        message = f"'{task}' is a High-priority task"
    case "medium":
        message = f"'{task}' is a Medium-priority task"
    case "low":
        message = f"'{task}' is a Low-priority task"
    case _:
        message = f"'{task}' is a Unknown-priority task"

if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    message += " that you can work on when convenient."

print("Provide a Customized Reminder\n")
print(message)
