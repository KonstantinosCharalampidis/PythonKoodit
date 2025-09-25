import random

def dice(sides):
    return random.randint(1, sides)

def diceroll(sides, target):
    if target > sides or target < 1:
        print("Target must be between 1 and", sides)
        return

    rolled = 0
    while rolled != target:
        rolled = dice(sides)
        print("You rolled:", rolled)

sides = int(input("Enter number of sides: "))
target = int(input("Enter target number: "))
diceroll(sides, target)


