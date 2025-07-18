
Task = input("Enter your task: ")
Priority = input("Enter the task's priority (high, medium, low): ").lower()
Time_bound = input("Is the task time-bound? (yes or no): ").lower()

match Priority:
    case "high":
        message = f"High-priority task: '{Task}'"
    case "medium":
        message = f"Medium-priority task: '{Task}'"
    case "low":
        message = f"Low-priority task: '{Task}'"
    case _:
        message = f"Unknown-priority task: '{Task}'"

if Time_bound == "yes":
    message += " that requires immediate attention today!"
else :
    message += " Consider completing it when you have free time."

print("\nReminder:", end=" ")
print(message)
