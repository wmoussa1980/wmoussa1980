# This program will use string functions/methods to parse the line.
# #  References:
# #    Programming Fundamentals – 2nd Edition
# #    Professor Dave Braunschweig
# #    W3schools Python Tutorial

def get_name():
    name = input("Please Enter your full name:")
    return name


def split_name(name):
    name_split = name.split()
    return name_split
 
        
def display_name(name_split):
    print("Your name in the form of (Lastname F):")
    print("{}, {}.".format(name_split[-1], name_split[0][0]))


def display_error():
    print("please provide complete name or try with space between names")

    
def main():
    name = get_name()
    name_split = split_name(name)
    if len(name_split) == 1 or len(name_split) == 0:
        display_error()
    else:
        display_name(name_split)


main()
