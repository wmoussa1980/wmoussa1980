# prompt the user for the name and the age of their dog.

print("Enter the name of your dog")
name = input()

print("Enter the age of your dog in human years")
age = float(input())

# Calculate the age of their dog in dog years.
dog_age = age * 7

# display the name and the age of their dog in dog years
print(name, "is", str(dog_age), "years old in dog years.")
