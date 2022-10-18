def displayExpression(value, count, product):
    print(str(value) + " * " + str(count) + " = " + str(product))

def getexpressions():
    print("enter expressions")
    expressions = int(input())
    
    return expressions

def getvalue():
    print("enter value")
    value = int(input())
    
    return value

def processExpressions(value, expressions):
    count = 1
    while count <= expressions:
        product = value * count
        displayExpression(value, count, product)
        count = count + 1

# Main
# # This program will ask the user to enter the value and the number of expressions to be displayed and then uses while loop to generate a list of multiplication expressions for a given value.
# 
# # References:
# #   Programming Fundamentals – 2nd Edition
value = getvalue()
expresions = getexpressions()
processExpressions(value, expresions)
