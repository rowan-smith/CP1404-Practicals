from prac_08.unreliable_car import UnreliableCar


def main():
    test = UnreliableCar("Test Car", 20, 30)
    test.drive(10)
    print(test)

if __name__ == '__main__':
    main()