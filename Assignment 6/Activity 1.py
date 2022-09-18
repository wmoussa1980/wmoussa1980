# This program will calculate weekly, monthly, and yearly gross pay.
# References:Programming Fundamentals – 2nd Edition


def calculate_weekly(hours, rate):
    weekly_pay = hours * rate
    
    return weekly_pay
  
    
def calculate_monthly(weekly_pay):
    monthly_pay = weekly_pay * 4
    
    return monthly_pay
   
    
def calculate_yearly(weekly_pay):
    yearly_pay = weekly_pay * 52
    
    return yearly_pay  


def get_rate():
    print("Enter rate per hour")
    rate = float(input())
    
    return rate


def get_hours():
    print("Enter hours number")
    hours = float(input())
    
    return hours


def display_result(weekly_pay, monthly_pay, yearly_pay):
    print("Weekly pay ", str(weekly_pay))
    print("Monthly pay ", float(monthly_pay))
    print("Yearly pay ", float(yearly_pay))
       
# Main


def main():
    
    hours = get_hours()
    rate = get_rate()
    weekly_pay = calculate_weekly(hours, rate)
    monthly_pay = calculate_monthly(weekly_pay)
    yearly_pay = calculate_yearly(weekly_pay)
    display_result(weekly_pay, monthly_pay, yearly_pay)

    
main()
