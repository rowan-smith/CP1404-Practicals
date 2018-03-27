from random import randint

MIN_NUMBER = 1
MAX_NUMBER = 45


def main():
    number_of_quick_picks = int(input("How many quick picks? "))
    values = []
    for i in range(number_of_quick_picks):
        for x in range(6):
            value = randint(MIN_NUMBER, MAX_NUMBER)
            while value in values:
                value = randint(MIN_NUMBER, MAX_NUMBER)
            values.append(value)
        values.sort()
        print("{:>2} {:>2} {:>2} {:>2} {:>2} {:>2}".format(values[0],
                                                           values[1],
                                                           values[2],
                                                           values[3],
                                                           values[4],
                                                           values[5]))
        values = []


main()
