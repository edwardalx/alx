from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current Date and Time:", formatted_date)
    return current_date

#display_current_datetime()



def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date:"))
    future_date =  display_current_datetime() + timedelta(days=number_of_days)
    formatted_future_date = future_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Future Date and Time:{formatted_future_date}")


calculate_future_date()

