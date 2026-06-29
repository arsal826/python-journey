# numbers = [15, 8, 23, 4, 42, 16, 7, 28, 11, 35]

# Without any built in functions:
# → Find the two largest numbers
# → Find the two smallest numbers
# → Print numbers divisible by both 3 and 4

numbers = [15, 8, 23, 4, 42, 16, 7, 28, 11, 35]
# find the two largest numbers
largest = float('-inf')
second_largest = float('-inf')
smallest = float('inf')
second_smallest = float('inf')
for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num
    if num < smallest:
        second_smallest = smallest
        smallest = num
    elif num < second_smallest and num != smallest:
        second_smallest = num

# print numbers divisible by both 3 and 4
print("Numbers divisible by both 3 and 4:")
for num in numbers:
    if num % 3 == 0 and num % 4 == 0:
        print(num)