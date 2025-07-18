
task = input("Enter your task: ")
priority = input("Enter the task's priority (high, medium, low): ").lower()
time_bound = input("Is the task time-bound? (yes or no): ").lower()

match priority:
    case "high":
        message = f"High-priority task: '{task}'"
    case "medium":
        message = f"Medium-priority task: '{task}'"
    case "low":
        message = f"Low-priority task: '{task}'"
    case _:
        message = f"Unknown-priority task: '{task}'"

if time_bound == "yes":
    message += " that requires immediate attention today!"

print("\nReminder:")
print(message)
