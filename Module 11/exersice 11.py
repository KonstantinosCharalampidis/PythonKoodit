class Publication:
    def __init__(self, name):
        self.name = name


class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        print("Book:")
        print(f"  Name: {self.name}")
        print(f"  Author: {self.author}")
        print(f"  Pages: {self.page_count}")


class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        print("Magazine:")
        print(f"  Name: {self.name}")
        print(f"  Chief editor: {self.chief_editor}")
class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


class ElectricCar(Car):
    def __init__(self, registration_number, max_speed, battery_capacity_kwh):
        super().__init__(registration_number, max_speed)
        self.battery_capacity_kwh = battery_capacity_kwh


class GasolineCar(Car):
    def __init__(self, registration_number, max_speed, tank_volume_liters):
        super().__init__(registration_number, max_speed)
        self.tank_volume_liters = tank_volume_liters


def main():
    print("publications")
    donald_duck = Magazine("Donald Duck", "Aki Hyppä")
    compartment_six = Book("Compartment No. 6", "Rosa Liksom", 192)

    donald_duck.print_information()
    print()
    compartment_six.print_information()

    print("cars")
    electric = ElectricCar("ABC-15", 180, 52.5)
    gasoline = GasolineCar("ACD-123", 165, 32.3)

    electric.current_speed = 100
    gasoline.current_speed = 120

    electric.drive(3)
    gasoline.drive(3)

    print(f"Electric car {electric.registration_number} drove {electric.travelled_distance} km.")
    print(f"Gasoline car {gasoline.registration_number} drove {gasoline.travelled_distance} km.")

    input("\nPress Enter to exit")


if __name__ == "__main__":
    main()
