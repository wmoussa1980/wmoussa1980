def calculateDogage(age):
    if age < 2:
        dogage = age * 10.5
    else:
        dogage = 21 + (age - 2) * 4
    
    return dogage

def displayResult(name, dogage):
    print(name + " is " + str(dogage) + " years old in dog years.")

def getAge():
    print("Enter the age of your dog in human years")
    age = float(input())
    
    return age

def getName():
    print("Enter the name of your dog")
    name = input()
    
    return name

# Main
# References:
# Programming Fundamentals – 2nd Edition
# Wikipedia: Aging in dogs
# This program will prompt the user for the name of their dog and its age in human years.
name = getName()
age = getAge()
dogage = calculateDogage(age)
displayResult(name, dogage)
