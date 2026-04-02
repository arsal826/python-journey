# Take this string:
# "welcome to python backend development"
# Capitalize the first letter of every word
# that is longer than 4 characters
# Leave short words as they are
# Expected: "welcome to Python Backend Development"

sentence = "welcome to python backend development"
final= []
for word in sentence.split():
    if len(word) > 4:
        final.append(word.capitalize())
    else:
        final.append(word)
result = " ".join(final)
print(result)

# You have:
# numbers = [10, 25, 3, 47, 8, 33, 15, 62, 7]

# Without using any built in functions
# Find and print:
# → The largest number
# → The smallest number  
# → The average

numbers = [10, 25, 3, 47, 8, 33, 15, 62, 7]
total = 0
max_number = numbers[0]
min_number = numbers[0]
second_lowest = numbers[0]
total = 0
second_largest = numbers[0]
for number in numbers:
    total += number
    if number>max_number:
        second_largest = max_number
        max_number = number
    elif number>second_largest and number!=max_number:
        second_largest = number    
    if number<min_number:
        second_lowest = min_number
        min_number = number
    elif number<second_lowest and number!=min_number:
        second_lowest = number
average = total / len(numbers)
print(f"Largest number: {max_number}")
print(f"Second largest number: {second_largest}")
print(f"Smallest number: {min_number}")
print(f"Second smallest number: {second_lowest}")
print(f"Average: {average}")