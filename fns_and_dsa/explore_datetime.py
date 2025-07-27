from datetime import datetime, timedelta, date

def display_current_datetime():
    current_date = datetime.now()
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time: ", formatted)

display_current_datetime()

num_of_days = int(input("Enter the number of days to add to the current date: "))

def calculate_future_date():
    future_date = date.today() + timedelta(days=num_of_days)
    formatted_future = future_date.strftime("%Y-%m-%d")  # ✅ Use strftime
    print("Future date: ", formatted_future)

calculate_future_date()
