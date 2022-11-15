def get_name():
    name = input("Please Enter your full name:")
    return name

def process(name):
    name_split = name.split()
    for word in name_split:
        word = word.strip 
        
def display(name_split):
        if len(name_split)==1:
            print("You have given only firstname, please provide complete name or try with space between names")
        else:
            print("Your name in the form of (Lastname F) where F is first initial of the firstname :")
            print("{} {}".format(name_split[1],name_split[0][0]))
    
def main():
    name = get_name()
    name_split = name.split()
    process(name)
    display(name_split)

main()
