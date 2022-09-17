# This program will calculate weekly, monthly, and yearly gross pay.
# References:Programming Fundamentals – 2nd Edition


def calculateWeekly_pay(hours, rate):
    weekly_pay = hours * rate
    
    return weekly_pay
  
    
def calculateMonthly_pay(weekly_pay):
    monthly_pay= weekly_pay * 4
    
    return monthly_pay
   
    
def calculateYearly_pay(weekly_pay):
    yearly_pay= weekly_pay * 52
    
    return yearly_pay  


def getRate():
    print("Enter rate per hour")
    rate = float(input())
    
    
    return rate


def getHours():
    print("Enter hours number")
    hours=float(input())
    
    return hours


def displayResult(weekly_pay, monthly_pay, yearly_pay):
    print("Weekly pay "  , str(weekly_pay))
    print("Monthly pay "  , float(monthly_pay))
    print("Yearly pay "  , float(yearly_pay))
       
# Main

def main():
    hours = getHours()
    rate = getRate()
    weekly_pay = calculateWeekly_pay(hours, rate)
    monthly_pay = calculateMonthly_pay(weekly_pay)
    yearly_pay = calculateYearly_pay(weekly_pay)
    displayResult(weekly_pay, monthly_pay, yearly_pay)

    
main()
