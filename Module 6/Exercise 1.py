import random
def dice():

    return random.randint(1,6)

def diceroll():
    rolled = 0
    while rolled !=6:
        rolled=dice()
        print("You rolled:",rolled)
diceroll()




