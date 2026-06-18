numbers = [12, 7, 23, 4, 9, 15, 8]
# Print the largest and smallest
# Print the average
largest = max(numbers)
smallest = min(numbers)
second_largest = 0
for num in numbers:
    if second_largest < num and num < largest:
        second_largest = num
average = sum(numbers) / len(numbers)
print(f"Largest number: {largest}")
print(f"Smallest number: {smallest}")
print(f"Second largest number: {second_largest}")
print(f"Average: {average:.2f}")
