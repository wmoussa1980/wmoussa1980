# This program will prompt the user for the name of their dog and its age in human years.
print("Enter the name of your dog")
name = input()
print("Enter the age of your dog in human years")
age = float(input())
dogage = age * 7
print(name + " is " + str(dogage) + " years old in dog years.")
