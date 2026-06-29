# numbers = [4, 7, 2, 9, 1, 5, 8, 3, 6, 7, 4, 2]
# → Remove duplicates keeping original order
# → Print sum and average
# → Print second largest number

numbers = [4, 7, 2, 9, 1, 5, 8, 3, 6, 7, 4, 2]
# Remove duplicates while preserving order
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
print("Unique numbers:", unique_numbers)
# Calculate sum and average
total_sum = sum(unique_numbers)
average = total_sum / len(unique_numbers)
print("Sum:", total_sum)
print("Average:", average)
# Print second largest number
largest = float('-inf')
second_largest = float('-inf')
for num in unique_numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif largest > num > second_largest:
        second_largest = num
print("Second largest number:", second_largest)