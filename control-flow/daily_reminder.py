
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        reminder = f"'{task}' is a High-priority task"
    case "medium":
        reminder = f"'{task}' is a Medium-priority task"
    case "low":
        reminder = f"'{task}' is a Low-priority task"
    case _:
        reminder = f"'{task}' is a Unknown-priority task"

if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += " that you can work on when convenient."

print("\n--- Daily Reminder ---")
print(reminder)
