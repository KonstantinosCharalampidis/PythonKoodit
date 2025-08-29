t = (float(input("Enter talents: ")))
p = float(input("Enter pounds: "))
l = float(input("Enter lots: "))

ppt = 20
lpp = 32
gpl =13.3

total_grams = (t * ppt * lpp * gpl + p * lpp * gpl + l * gpl)
kilograms = (total_grams // 1000)
grams = total_grams % 1000
print("The weight in modern units is:", kilograms,"and",grams)


