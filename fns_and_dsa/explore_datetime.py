import datetime




def display_current_datetime():
    current_date = datetime.datetime.now()
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time: ", formatted)

display_current_datetime()





num_of_days = int(input("Enter the number of days to add to the current date: "))

def calculate_future_date():
    future_date = datetime.date.today() + datetime.timedelta(days=num_of_days)
    print("Future date: ", future_date)

calculate_future_date()

