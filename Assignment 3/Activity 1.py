print("rate per hour")
rate = float(input())
print("hours worked per week")
hours = float(input())
weekly = hours * rate
monthly = weekly * 4
yearly = weekly * 52
print("Weekly " + str(weekly))
print("Monthly " + str(monthly))
print("Yearly " + str(yearly))
