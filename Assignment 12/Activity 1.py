# This program will use dynamic array.
# #  References:
# #    Programming Fundamentals – 2nd Edition
# #    Professor Dave Braunschweig
# W3schools Python Tutorial
def get_scores():
    scores = [] 
    while True: 
        score = get_score()
        if score < 0:
            break
        else:
            scores.append(score)
    return scores
 
    
def get_score():
    score = int(input("Enter the score or negative number to exit: "))
    return score
 
    
def calculate_average(scores):
    total = 0
    for n in scores:
        total = total + n
    average = total / len(scores)
    return average


def calculate_max(scores):
    maximum = max(scores)
    return maximum


def calculate_min(scores):
    minimum = min(scores)
    return minimum


def display_results(average, minimum, maximum):
    print("The average of the scores is: " + str(average))
    print("The maximum score is: " + str(maximum))
    print("The minimum score is: " + str(minimum))

    
def main():
    scores = get_scores()
    average = calculate_average(scores)
    maximum = max(scores)
    minimum = min(scores)
    calculate_max(scores)
    calculate_min(scores)
    display_results(average, minimum, maximum)
 

main()
