from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    silver_taxi1 = SilverServiceTaxi("Hummer", 200, 2)
    silver_taxi1.start_fare()
    silver_taxi1.drive(18)
    print(silver_taxi1)
    print("Fare Price: ${:.2f}".format(silver_taxi1.get_fare()))

if __name__ == '__main__':
    main()
