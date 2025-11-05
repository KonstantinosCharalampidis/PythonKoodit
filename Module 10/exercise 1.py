class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.floor = bottom
    def floor_up(self):
        if self.floor < self.top:
            self.floor += 1
            print("Elevator goes up to floor", self.floor)
    def floor_down(self):
        if self.floor > self.bottom:
            self.floor -= 1
            print("Elevator goes down to floor", self.floor)
    def go_to_floor(self, target):
        print("\nElevator moving from floor", self.floor, "to floor", target)
        while self.floor < target:
            self.floor_up()
        while self.floor > target:
            self.floor_down()
        print("Elevator arrived at floor", self.floor)
class Building:
    def __init__(self, bottom, top, num_elevators):
        self.bottom = bottom
        self.top = top
        self.elevators = []
        for i in range(num_elevators):
            elevator = Elevator(bottom, top)
            self.elevators.append(elevator)
    def run_elevator(self, number, target_floor):
        print("\nRunning elevator", number, "to floor", target_floor)
        self.elevators[number - 1].go_to_floor(target_floor)
    def fire_alarm(self):
        print("\n*** FIRE ALARM! ***")
        print("All elevators going to bottom floor.")
        for i, e in enumerate(self.elevators):
            print("Elevator", i + 1, "moving to bottom floor...")
            e.go_to_floor(self.bottom)
def main():
    print("ELEVATOR TEST")
    building = Building(1, 10, 3)
    building.run_elevator(1, 5)
    building.run_elevator(2, 8)
    building.fire_alarm()
if __name__ == "__main__":
    main()

