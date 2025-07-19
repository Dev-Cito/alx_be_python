
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


custom_note = Task
reminder_date = input("\nReminder date (optional, DD-MM-YYYY): ")
reminder_time = input("Reminder time (optional, e.g., 2:00 PM): ")

if custom_note or reminder_date or reminder_time:
    print("\n🔔 Your reminders:")
    if custom_note:
        print(f"   📝 Note: {custom_note}")
    if reminder_date:
        print(f"   📅 Date: {reminder_date}")
    if reminder_time:
        print(f"   ⏰ Time: {reminder_time}")



