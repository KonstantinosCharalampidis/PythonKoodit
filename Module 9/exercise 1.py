import random
class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0
    def accelerate(self, change_in_speed):
        self.current_speed = self.current_speed + change_in_speed
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        if self.current_speed < 0:
            self.current_speed = 0
    def drive(self, hours):
        self.travelled_distance = self.travelled_distance + (self.current_speed * hours)
    def print_info(self):
        print(f"{self.registration_number}:")
        print(f"  Max speed: {self.maximum_speed} km/h")
        print(f"  Current speed: {self.current_speed} km/h")
        print(f"  Travelled distance: {self.travelled_distance:.1f} km")
        print()
cars = []
for i in range(1, 11):
    reg_number = "ABC-" + str(i)
    max_speed = random.randint(100, 200)
    new_car = Car(reg_number, max_speed)
    cars.append(new_car)
race_finished = False
hour = 0
while not race_finished:
    hour = hour + 1
    for car in cars:
        speed_change = random.randint(-10, 15)
        car.accelerate(speed_change)
        car.drive(1)
        if car.travelled_distance >= 10000:
            race_finished = True
print("\n🏁 Race finished! Final results:")
print(f"{'Car':<8}{'Max Speed':<12}{'Current Speed':<15}{'Distance (km)':<15}")
print("-" * 50)
for car in cars:
    print(f"{car.registration_number:<8}{car.maximum_speed:<12}{car.current_speed:<15}{car.travelled_distance:<15.1f}")
