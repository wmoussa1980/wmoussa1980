# this program will calculate weekly, monthly, and yearly gross pay.
# References:Programming Fundamentals – A Modular Structured Approach, 2nd Edition
print("Enter rate per hour")
rate = float(input())
print("Enter hours number")
hours = float(input())
weekly = float(hours) * float(rate)
monthly = weekly * 4
yearly = weekly * 52
print("Weekly pay " + str(weekly))
print("Monthly pay " + str(monthly))
print("Yearly pay " + str(yearly))
