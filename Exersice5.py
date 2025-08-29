wage = float(input("What is your hourly wage?: "))
h = float(input("How many hours did you work?: "))
day = input("What day is it? ")

if day == "Sunday":
    print("Daily wages", (wage * h)*2)
else:
    print(f"{day}'s wage is, {wage * h}")