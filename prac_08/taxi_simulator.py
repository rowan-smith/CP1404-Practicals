from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU_TEXT = """q)uit, c)hoose taxi, d)rive\n>>> """


def main():
    print("Let's drive!")
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    user_choice = input(MENU_TEXT).upper()
    while user_choice != "Q":
        if user_choice == "C":
            taxi_choice = choose_taxi(taxis)
        elif user_choice == "D":
            drive_taxi(taxis, taxi_choice)
        user_choice = input(MENU_TEXT).upper()


def drive_taxi(taxis, choice):
    distance = int(input("Drive how far? "))
    taxis[choice].drive(distance)
    print("Your {} trip cost you ${:.2f}".format(taxis[choice].name, taxis[choice].get_fare()))
    print("Bill to date: ${:.2f}".format(taxis[choice].get_fare()))


def choose_taxi(taxis):
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))
    chosen_taxi = int(input("Choose taxi: "))
    print("Bill to date: ${:.2f}".format(taxis[chosen_taxi].get_fare()))
    return chosen_taxi


if __name__ == '__main__':
    main()
