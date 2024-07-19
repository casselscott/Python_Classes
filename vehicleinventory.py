# Parent class
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Vehicle: {self.year} {self.make} {self.model}")

# Child class Car inheriting from Vehicle
class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def display_info(self):
        super().display_info()
        print(f"Type: Car, Doors: {self.num_doors}")

    def drive(self):
        print(f"{self.make} {self.model} is now driving.")

# Child class Motorcycle inheriting from Vehicle
class Motorcycle(Vehicle):
    def __init__(self, make, model, year, num_wheels):
        super().__init__(make, model, year)
        self.num_wheels = num_wheels

    def display_info(self):
        super().display_info()
        print(f"Type: Motorcycle, Wheels: {self.num_wheels}")

    def accelerate(self):
        print(f"{self.make} {self.model} is accelerating.")

# Main program
if __name__ == "__main__":
    # Create instances of Car and Motorcycle
    car1 = Car("Toyota", "Camry", 2020, 4)
    motorcycle1 = Motorcycle("Harley-Davidson", "Sportster", 2021, 2)

    # Display information
    car1.display_info()
    car1.drive()
    print()
    motorcycle1.display_info()
    motorcycle1.accelerate()
