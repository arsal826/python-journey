numbers = [3, 7, 1, 9, 4, 7, 3, 8, 1, 5]
# → Remove duplicates
# → Find largest and smallest without max/min
# → Print numbers divisible by 3
# Remove duplicates
unique_numbers = []
for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)
print("Unique numbers:", unique_numbers)
# Find largest and smallest without max/min
largest = numbers[0]
smallest = numbers[0]
for number in numbers:
    if number > largest:
        largest = number
    if number < smallest:
        smallest = number
print("Largest number:", largest)
print("Smallest number:", smallest)
# Print numbers divisible by 3
for number in numbers:
    if number % 3 == 0:
        print("Divisible by 3:", number)
        