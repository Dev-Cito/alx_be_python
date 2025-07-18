
Task = input("Enter your task:")
Priority = input("Priority (high/medium/low):").lower()
Time_bound = input("Is it time-bound? (yes/no):").lower()

match Priority:
    case "high":
        message = f"'{Task}' is a High-priority task"
    case "medium":
        message = f"'{Task}' is a Medium-priority task"
    case "low":
        message = f"'{Task}' is a Low-priority task."
    case _:
        message = f"'{Task}' is a Unknown-priority task"

if Time_bound == "yes":
    message += " that requires immediate attention today!"
    print("\nReminder:", end=" ")
    print(message)
elif Time_bound == "no":
    message += " Consider completing it when you have free time."
    print("\nNote:", end=" ")
    print(message)
else :
    print("Invalid time bound!")


