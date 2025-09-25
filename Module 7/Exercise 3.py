airports = {}

while True:
    print("1 = Add airport")
    print("2 = Get airport")
    print("3 = Quit")

    choice = input("Choose: ")

    if choice == "1":
        code = input("ICAO code: ")
        name = input("Airport name: ")
        airports[code] = name

    elif choice == "2":
        code = input("ICAO code: ")
        if code in airports:
            print("Airport:", airports[code])
        else:
            print("Not found")

    elif choice == "3":
        print("Goodbye!")
        break
