
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        print(f"Reminder:'{task}' is a High-priority task ",end="")
    case "medium":
        print(f"Reminder:'{task}' is a Medium-priority task ", end="")
    case "low":
        print(f"Note:'{task}' is a Low-priority task ", end="")
    case _:
        print(f"Note:'{task}' is a Unknown-priority task ", end="")

if time_bound == "yes":
    print("that requires immediate attention today!")
else:
    print("that you can work on when convenient.")

