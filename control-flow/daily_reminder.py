
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        Reminder = f"'{task}' is a High-priority task"
    case "medium":
        Reminder = f"'{task}' is a Medium-priority task"
    case "low":
        Reminder = f"'{task}' is a Low-priority task"
    case _:
        Reminder = f"'{task}' is a Unknown-priority task"

if time_bound == "yes":
    Reminder += " that requires immediate attention today!"
else:
    Reminder += " that you can work on when convenient."

print("Provide a Customized Reminder\n")
print(Reminder)
