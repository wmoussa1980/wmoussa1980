def calculateaverage(count, total):
    average = float(total) / count
    
    return average

def displayaverage(total, count, average):
    print("The average is " + str(average))

def getgrade():
    print("Enter grade (enter negative value to stop) ")
    grade = int(input())
    
    return grade

def processinput():
    total = 0
    count = 0
    while True:    #This simulates a Do Loop
        grade = getgrade()
        total = total + grade
        count = count + 1
        if not(grade >= 0): break   #Exit loop
    average = calculateaverage(count, total)
    displayaverage(count, total, average)
    
    return average

# Main
# This program will ask the user to enter grade scores and use a loop to request each score and add it to a total. Also will continue accepting scores until the user enters either a negative value. Finally, the program will calculate and display the average for the entered scores.
# #  References:
# #    Programming Fundamentals – 2nd Edition
processinput()
