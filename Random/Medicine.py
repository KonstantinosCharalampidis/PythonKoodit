age = int(input("How old are you?: "))

if 15 <= age <18:
    weight = float(input("How much do you wight? "))

if age >= 18 or age >=15 and weight >= 55:
    print("You can use this medicine")
else:
    print("You cannot use this medicine")