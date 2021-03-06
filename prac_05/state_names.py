"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting

Psduocode:

loop state in STATE_NAMES
    display formatted state code "is" state
"""

STATE_NAMES = {"QLD": "Queensland",
               "NSW": "New South Wales",
               "NT": "Northern Territory",
               "WA": "Western Australia",
               "ACT": "Australian Capital Territory",
               "VIC": "Victoria", "TAS": "Tasmania"}


def main():
    state = input("Enter short state: ").upper()
    while state != "":
        if state in STATE_NAMES:
            print(state, "is", STATE_NAMES[state])
        else:
            print("Invalid short state")
        state = input("Enter short state: ").upper()

    for state in STATE_NAMES:
        print("{:<4} is {}".format(state, STATE_NAMES[state]))


main()
