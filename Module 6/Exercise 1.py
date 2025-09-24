import random
def dice():
    number=random.randint(1,6)
    return number

def diceroll():
    rolled = 0
    while rolled !=6:
        rolled=dice()
        print("You rolled:",rolled)
diceroll()
