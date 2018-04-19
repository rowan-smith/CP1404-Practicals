from prac_07.guitar import Guitar


def main():
    guitars = []
    print("My guitars!")
    guitar_name = input("Name: ")
    guitar_year = int(input("Year: "))
    guitar_cost = float(input("Cost: $"))
    guitars.append(Guitar(guitar_name, guitar_year, guitar_cost))
    print("{} ({}) : {} added.".format(guitar_name, guitar_year, guitar_cost))
    while guitar_name != "":
        guitar_name = input("Name: ")
        guitar_year = int(input("Year: "))
        guitar_cost = float(input("Cost: $"))
        guitars.append(Guitar(guitar_name, guitar_year, guitar_cost))
        print("{} ({}) : {} added.".format(guitar_name, guitar_year, guitar_cost))

    for i, guitar in enumerate(guitars):
        print("Guitar {}: {:>30} ({}), worth ${:10,.2f} {}".format(i + 1,
        guitar.name, guitar.year, guitar.cost, "(Vintage)" if guitar.is_vintage() else ""))


main()
