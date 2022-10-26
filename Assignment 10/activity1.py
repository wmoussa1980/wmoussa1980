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
processinput()
