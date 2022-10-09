def forloop(value, number):
    for n in range(1, number + 1, 1):
        print(str(value) + " x " + str(n) + " = " + str(value * n))

def getnumber():
    print("enter expresion number")
    number = float(input())
    
    return number

def getvalue():
    print("enter value")
    value = float(input())
    
    return value

# Main
number = getnumber()
value = getvalue()
forloop(value, number)
