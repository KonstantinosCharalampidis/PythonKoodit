import math

def pizza_price(diameter_cm, price):
    radius_m = (diameter_cm / 100) / 2
    area_m2 = math.pi * radius_m * radius_m
    return price / area_m2

d1 = float(input("Pizza 1 diameter (cm): "))
p1 = float(input("Pizza 1 price (€): "))

d2 = float(input("Pizza 2 diameter (cm): "))
p2 = float(input("Pizza 2 price (€): "))

u1 = pizza_price(d1, p1)
u2 = pizza_price(d2, p2)

print("Pizza 1 unit price:", round(u1, 2), "€/square meter")
print("Pizza 2 unit price:", round(u2, 2), "€/square meter")

if u1 < u2:
    print("Pizza 1 is better value.")
elif u2 < u1:
    print("Pizza 2 is better value.")
else:
    print("Both pizzas have the same value.")
