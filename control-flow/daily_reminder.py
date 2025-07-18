

task = input("Enter a task :")

priority = input("Priority(high, low, medium) :").lower()

time_bound = input("is it time sensitive(yes, no) :").lower()

days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

match priority :
    case "high" :
        while time_bound == "yes":
            print(f"\nReminder\nfrom {days[0]} to {days[3]} remember a {task} task you have!\n")
            print(f"{task} is a high priority task that requires immediate attention today!\n")
            break
        else :
            print(f"{task} is a high priority task that requires immediate attention today!\n")

    case "low" :
        while time_bound == "yes":
            print(f"\nReminder\n we are on {days[6]}, what an amazing a weekend!\n")
            print(f"{task} is a low priority task. Consider to complete it when you have free time.")
            break
        else :
            print(f"{task} is a low priority task. Take your time, you might complete it at anytime.")

    case "medium" :
        while time_bound == "yes":
            print(f"\nReminder\nfrom {days[4]} to {days[5]} remember a {task} task you have!\n")
            print(f"{task} is a medium priority task. Consider completing it soon.")
            break
        else:
            print(f"{task} is a medium priority task. start thinking about completing it.")

    case _:
            print("Unknown time priority, please insert a valid one!")




