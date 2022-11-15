def get_name():
    name = input("Please Enter your full name:")
    return name


def process_input(name):
    name_split = name.split()
    for word in name_split:
        word = word.strip
        if len(name_split) == 1:
            display_error()
        else:
            display_name(name_split)
        return name_split

    
def display_name(name_split):
    print("Your name in the form of (Lastname F) ")
    print("{}, {}.".format(name_split[1], name_split[0][0]))

    
def display_error():
    print("please provide complete name or try with space between names")
 

def main():
    name = get_name()
    process_input(name)

    
main()  
