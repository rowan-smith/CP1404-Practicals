from prac_07.guitar import Guitar


def main():
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2012, 0)
    memphis = Guitar("Memphis Les Paul", 1970, 5285.16)
    hofner = Guitar("Hofner Super Solid III", 1963, 942.91)
    gibson2 = Guitar("Gibson Les Paul Standard", 1983, 3210.09)

    guitars = [gibson, another_guitar, memphis, hofner, gibson2]

    for guitar in guitars:
        print("Name:", guitar.name)
        print("Vintage:", guitar.is_vintage())


main()
