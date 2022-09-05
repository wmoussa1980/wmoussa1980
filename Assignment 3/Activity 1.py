# this program will calculate weekly, monthly, and yearly gross pay.
# References:Programming Fundamentals – A Modular Structured Approach, 2nd Edition
print("rate")
rate = float(input())
print("hours")
hours = float(input())
weekly = hours * rate
monthly = weekly * 4
yearly = weekly * 52
print("Weekly " + str(weekly))
print("Monthly " + str(monthly))
print("Yearly " + str(yearly))
