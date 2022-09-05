print("Enter rate")
rate = float(input())
print("Enter hours")
hours = float(input())
weekly = hours * rate
monthly = weekly * 4
yearly = weekly * 52
print("Weekly pay is " + str(weekly))
print("Monthly pay is " + str(monthly))
print("Yearly gross pay is " + str(yearly))
