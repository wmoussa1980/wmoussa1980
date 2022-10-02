# This program will calculate weekly, monthly, and yearly gross pay.

# References:
#   Programming Fundamentals – 2nd Edition


def calculate_weekly(hours, rate):
    weekly_pay = hours * rate    
    return weekly_pay
  
    
def over(hours,rate):
    over_time =(40*rate)+((hours-40)*1.5)*rate
    return over_time


def get_rate():
    print("Enter rate per hour")
    rate = float(input())
    return rate


def get_hours():
    print("Enter hours number")
    hours = float(input())
    return hours


def display_result(over_time):
    print("Weekly pay with Overtime is ", float(over_time))
    
    
def result(weekly_pay):
    print("Weekly pay is ", str(weekly_pay))


def main():    
    hours = get_hours()
    rate = get_rate()
    
    weekly_pay = calculate_weekly(hours, rate)
    over_time = over(hours, rate)
    
    if hours<=40 :
        weekly_pay = calculate_weekly(hours, rate)
        result(weekly_pay)

    elif hours> 40:
        over_time = over(hours, rate)
        display_result(over_time)
           
main()
