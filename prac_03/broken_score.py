"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    score = float(input("Enter score: "))
    result = score_result(score)
    print(result)


def score_result(score):
    if score < 0:
        return "Invalid score"
    else:
        if score > 100:
            return "Invalid score"
        if score > 90:
            return "Excellent"
        if score > 50:
            return "Passable"
        if score < 50:
            return "Bad"


main()
