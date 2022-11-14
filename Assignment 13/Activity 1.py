name=input("Please Enter your full name:")

l=name.split()
for word in l:
    word=word.strip 
if len(l)==1:
    print("You have given only firstname , please provide complete name or try with space between names")
else:
        print("Your name in the form of (Lastname F) where F is first initial of the firstname :")
        print("{} {}".format(l[1],l[0][0]))
