print("Enter hourly rate")
hourlyrate = float(input())
print("Enter weekly hours")
weeklyhours = float(input())
weeklypay = weeklyhours * hourlyrate
monthlypay = weeklypay * 4
yearlypay = weeklypay * 52
print("Weekly pay is" + str(weeklypay))
print("Monthly pay is " + str(monthlypay))
print("Yearly gross pay is " + str(yearlypay))
