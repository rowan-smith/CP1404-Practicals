from prac_08.car import Car
from random import randint


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        random_reliability = randint(0, 100)
        if random_reliability < self.reliability:
            super().drive(distance)
        return distance

