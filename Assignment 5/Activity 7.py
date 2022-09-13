# References:Programming Fundamentals – A Modular Structured Approach, 2nd Edition

def calculateDogage(age):
    dogage = age * 7
    
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
# This program will prompt the user for the name of their dog and its age in human years.
name = getName()
age = getAge()
dogage = calculateDogage(age)
displayResult(name, dogage)
