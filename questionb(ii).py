def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


numbers = [9, 2, 3, 5, 8]
result = sum_list(numbers)
print("Sum of the numbers in the list is:", result)