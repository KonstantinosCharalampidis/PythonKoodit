while True:
    g = float(input("Gallons: "))
    if g < 0:
        print("Gallons cannot be negative")
        break
    print(g * 3.78541)
