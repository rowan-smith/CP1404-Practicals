from prac_07.car import Car


def main():
    my_car = Car(180)
    my_car.drive(30)
    my_car.name = "Car"
    print("Car Fuel =", my_car.fuel)
    print("Car Odo =", my_car.odometer)
    print(my_car)

    limo = Car(100)
    limo.add_fuel(20)
    print("Limo Fuel:", limo.fuel)
    limo.drive(115)
    print("Limo Odo", limo.odometer)

main()
