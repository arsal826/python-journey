# Create this list:
#    numbers = [4, 7, 2, 9, 1, 5, 8, 3, 6]
#    Without using sort() or sorted()
#    Print the list in ascending order
#    Hint: compare pairs and swap

numbers = [4, 7, 2, 9, 1, 5, 8, 3, 6]
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]
print(numbers)

#  Take a list of numbers
#    Return a new list with only unique values
#    numbers = [1, 2, 2, 3, 4, 4, 4, 5, 1]
#    Expected: [1, 2, 3, 4, 5]
#    No using set()

numbers = [1, 2, 2, 3, 4, 4, 4, 5, 1]
unique_numbers = [] 
for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)
print(unique_numbers)

# Flatten this nested list into one list:
#    nested = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
#    Expected: [1, 2, 3, 4, 5, 6, 7, 8, 9]

nested = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flattened = []
for inner_list in nested:
    for num in inner_list:
        flattened.append(num)
print(flattened)

#  Take two lists
#     Find the common items between them
#     list1 = [1, 2, 3, 4, 5]
#     list2 = [3, 4, 5, 6, 7]
#     Expected: [3, 4, 5]
#     No using set()
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
unique_numbers = []
for num in list1:
    if num in list2:
        unique_numbers.append(num)
print(unique_numbers)

# Take a list of names
#    Remove all names that start with the 
#    letter "A"
#    names = ["Arsal","Ahmed","Sara","Ali","Bob"]
#    Expected: ["Sara", "Bob"]
names = ["Arsal","Ahmed","Sara","Ali","Bob"]
filtered_names = []
for name in names:
    if name.startswith("A"):
        names.pop(names.index(name))
print(names)

names = ["Arsal","Ahmed","Sara","Ali","Bob"]
filtered_names = []
for name in names:
    if not name.startswith("A"):
        filtered_names.append(name)
print(filtered_names)

