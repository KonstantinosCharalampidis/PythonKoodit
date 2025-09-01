numbers = []
while True:
    num = input("Enter a number or press ENTER to quit: ")
    if num == "":
        break
    numbers.append(float(num))
print("Smallest number: ",min(numbers))
print("Largest number: ",max(numbers))