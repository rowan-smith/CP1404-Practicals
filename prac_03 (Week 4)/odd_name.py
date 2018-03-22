"""Rowan"""

user_name = input("Please enter your name: ")
while len(user_name) < 1:
    print("Name is less than 1 character!")
    user_name = input("Please enter your name: ")

for x in range(1, len(user_name), 2):
    print(user_name[x])