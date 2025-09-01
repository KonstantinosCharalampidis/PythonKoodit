import random
n = random.randint(1,10)
while True:
    guess= int(input("Guess the correct number between 1-10: "))
    if guess > n:
        print("Too high")
    elif guess < n:
        print("Too low")
    else:
        print("Correct!")
        break



