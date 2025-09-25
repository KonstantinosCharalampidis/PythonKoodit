def sum_list(numbers):
    total = 0
    for n in numbers:
        total = total + n
    return total

my_list = [1, 2, 3, 4, 5]
print("List:", my_list)
print("Sum:", sum_list(my_list))
