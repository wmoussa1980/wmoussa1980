def displayExpression(value, count, product):
    product = value * count
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
    for count in range(1, expressions + 1, 1):
        product = value * count
        displayExpression(value, count, product)

# Main
# # This program will ask the user to enter the value and the number of expressions to be displayed and then uses a loop to generate a list of multiplication expressions for a given value.
# 
# # References:
# #   Programming Fundamentals – 2nd Edition
value = getvalue()
expresions = getexpressions()
processExpressions(value, expresions)
