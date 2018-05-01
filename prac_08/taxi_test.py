from prac_08.taxi import Taxi


def main():
    taxi1 = Taxi('Prius 1', 100)
    taxi1.drive(40)
    print(taxi1)
    print("${}".format(taxi1.get_fare()))
    taxi1.start_fare()
    taxi1.drive(100)
    print(taxi1)
    print("${}".format(taxi1.get_fare()))

if __name__ == '__main__':
    main()
