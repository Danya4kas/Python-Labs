from abc import ABC, abstractmethod

class Transport(ABC):
    def __init__(self, name, speed, capacity):
        self.name = name
        self.speed = speed
        self.capacity = capacity

    @abstractmethod
    def move(self, distance):
        pass

    @abstractmethod
    def fuel_consumption(self, distance):
        pass

    @abstractmethod
    def info(self):
        pass

    def calculate_cost(self, distance, price_per_unit):
        return self.fuel_consumption(distance) * price_per_unit

class Car(Transport):
    def move(self, distance):
        return distance / self.speed

    def fuel_consumption(self, distance):
        return distance * 0.07

    def info(self):
        return f"Car: {self.name}, speed: {self.speed} km/h, capacity: {self.capacity}"

class Bus(Transport):
    def __init__(self, name, speed, capacity, passengers):
        super().__init__(name, speed, capacity)
        self.passengers = passengers

    def move(self, distance):
        return distance / self.speed

    def fuel_consumption(self, distance):
        if self.passengers > self.capacity:
            print("Перевантажено!")
            return 0 
        return distance * 0.15

    def info(self):
        return f"Bus: {self.name}, speed: {self.speed} km/h, capacity: {self.capacity}, passengers: {self.passengers}"

class Bicycle(Transport):
    def __init__(self, name, speed, capacity):
        super().__init__(name, speed, capacity)
        if self.speed > 20:
            self.speed = 20  

    def move(self, distance):
        return distance / self.speed

    def fuel_consumption(self, distance):
        return 0

    def info(self):
        return f"Bicycle: {self.name}, speed: {self.speed} km/h, capacity: {self.capacity}"

class ElectricCar(Car):
    def fuel_consumption(self, distance):
        return 0 

    def battery_usage(self, distance):
        return distance * 0.2

    def calculate_cost(self, distance, price_per_unit):
        return self.battery_usage(distance) * price_per_unit


transports = [
    Car("Ford", 120, 5),
    Bus("Bus", 85, 51, 20),  
    Bus("City Bus", 60, 30, 55),   
    Bicycle("Bike", 25, 1),  
    ElectricCar("Tesla", 115, 5)
]

for t in transports:
    print(t.info())
    print("Час у дорозі:", t.move(100))
    print("Витрати пального:", t.fuel_consumption(100))
    print("Вартість:", t.calculate_cost(100, 2.0))