numbers=[]
while True:
    nums=input("Enter number: ")
    if nums == "":
        break
    numbers.append(nums)
numbers.sort(reverse=True)
print(numbers)



