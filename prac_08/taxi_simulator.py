from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU_TEXT = """q)uit, c)hoose taxi, d)rive\n>>> """


def main():
    print("Let's drive!")
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    bill_total = 0
    user_choice = input(MENU_TEXT).upper()
    while user_choice != "Q":
        if user_choice == "C":
            taxi_choice = choose_taxi(taxis, bill_total)
        elif user_choice == "D":
            bill_total = drive_taxi(taxis, taxi_choice, bill_total)
        user_choice = input(MENU_TEXT).upper()
    print("Total trip cost ${:.2f}".format(bill_total))
    print_taxis(taxis)


def drive_taxi(taxis, choice, bill_total):
    distance = int(input("Drive how far? "))
    taxis[choice].drive(distance)
    print("Your {} trip cost you ${:.2f}".format(taxis[choice].name, taxis[choice].get_fare()))
    bill_total = bill_total + taxis[choice].get_fare()
    print("Bill to date: ${:.2f}".format(bill_total))
    return bill_total


def choose_taxi(taxis, bill_total):
    print_taxis(taxis)
    chosen_taxi = int(input("Choose taxi: "))
    print("Bill to date: ${:.2f}".format(bill_total))
    return chosen_taxi


def print_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


if __name__ == '__main__':
    main()
