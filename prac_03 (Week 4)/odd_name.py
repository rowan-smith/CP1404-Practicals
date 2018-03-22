"""Rowan"""


def get_name():
    user_name = input("Please enter your name: ")
    while len(user_name) < 1:
        print("Name is less than 1 character!")
        user_name = input("Please enter your name: ")

    print_name(user_name)


def print_name(user_name, letters=2):
    for x in range(0, len(user_name), letters):
        print(user_name[x])

get_name()
