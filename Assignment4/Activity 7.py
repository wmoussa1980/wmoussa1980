# This program will prompt the user for the name of their dog and its age in human years.
# This program will calculate and display the age of their dog in dog years, based on the popular myth that one human year equals seven dog years.
print("Enter the name of your dog")
name = input()
print("Enter the age of your dog in human years")
age = float(input())
dogage = age * 7
print(name + " is " + str(dogage) + " years old in dog years.")
