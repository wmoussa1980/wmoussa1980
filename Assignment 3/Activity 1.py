# this program will calculate weekly, monthly, and yearly gross pay.
# References:Programming Fundamentals – A Modular Structured Approach, 2nd Edition
print("Enter rate per hour")
rateperhour = float(input("rate per hour"))
print("Enter hours number")
hoursnumber = float(input("hours"))
weekly = hoursnumber * rateperhour
monthly = weekly * 4
yearly = weekly * 52
print("Weekly pay " + str(weekly))
print("Monthly pay " + str(monthly))
print("Yearly pay " + str(yearly))
