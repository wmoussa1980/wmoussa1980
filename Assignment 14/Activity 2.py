
def read_file():
    try:
        with open("scores.txt", "r") as file:
            file.readline()
            scores_array = []
            while True:
                content = file.readline()
                if not content:
                    break
                split_str = content.split(',')
                scores_array.append(int(split_str[1].rstrip()))
                scores = scores_array
    except Exeption as e:
        print(e)
        print("Error reading", "scores.text")
    return scores


def calculate_average(scores):
    total = 0
    for n in scores:
        total = total + n
    average = total / len(scores)
    return average


def calculate_max(scores):
    high = max(scores)
    return high


def calculate_min(scores):
    low = min(scores)
    return low


def display_results(scores, average, minimum, maximum):
    print("Score Array contents are : ")
    print(scores)
    print("The average of the scores is: " + str(average))
    print("The high score is: " + str(maximum))
    print("The low score is: " + str(minimum))


def main():
    scores = read_file()
    average = calculate_average(scores)
    high = calculate_max(scores)
    low = calculate_min(scores)
    display_results(scores, average, low, high)


main()
