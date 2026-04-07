# Take this sentence:
# "the quick brown fox jumps over the lazy dog"
# Print every word that contains the letter 'o'
# Expected: quick? No. brown? Yes. fox? Yes...
# find them all.
from day3.p9 import class_average


new_words = []
sentence = "the quick brown fox jumps over the lazy dog"
# split the sentence into words
words = sentence.split()
# loop through the words and check if they contain 'o'
for word in words:
    if 'o' in word:
        new_words.append(word)
print(new_words)



# Write a function called remove_duplicates(lst)
# It takes a list and returns a new list
# with duplicates removed, keeping original order

# remove_duplicates([3,1,2,1,3,4,2]) → [3,1,2,4]

# No using set()

def remove_duplicates(lst):
    new_lst = []
    for item in lst:
        if item not in new_lst:
            new_lst.append(item)
    return new_lst

# Test the function
numbers = [3,1,2,1,3,4,2]
result = remove_duplicates(numbers)
print(result)


inventory = {
    "apples": 50,
    "bananas": 12,
    "oranges": 3,
    "grapes": 8,
    "mangoes": 25
}

# Print only items where quantity is below 10
# Then print total number of items in inventory
# Then print the item with highest quantity

# Print items with quantity below 10
for item, quantity in inventory.items():
    if quantity < 10:
        print(f"{item}: {quantity}")

# Print total number of items in inventory
total_items = sum(inventory.values())
print(f"Total items in inventory: {total_items}")

# Print the item with highest quantity
for item, quantity in inventory.items():
    if quantity == max(inventory.values()):
        print(f"Item with highest quantity: {item} ({quantity})")

# Take this sentence:
# "apple banana apple orange banana apple"
# Count each word using a dictionary
# Then print the most repeated word

sentence = "apple banana apple orange banana apple"
word_count = {}
for word in sentence.split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Print the most repeated word
for word, count in word_count.items():
    if count == max(word_count.values()):
        print(f"The most repeated word is: {word} ({count} times)")


# # Write a function called summarize(students)
# # It takes this list:
# students = {
#     {"name": "Arsal", "grade": 85},
#     {"name": "Ahmed", "grade": 92},
#     {"name": "Sara",  "grade": 67},
#     {"name": "Ali",   "grade": 78},
#     {"name": "Zara",  "grade": 55}
# }
# It should print:
# → Total students
# → Class average
# → Highest scorer name
# → Lowest scorer name
# → How many passed (grade >= 60)
# → How many failed (grade < 60)

students = [
    {"name": "Arsal", "grade": 85},
    {"name": "Ahmed", "grade": 92},
    {"name": "Sara",  "grade": 67},
    {"name": "Ali",   "grade": 78},
    {"name": "Zara",  "grade": 55}
]

def summarize(students):
    highest_scorer = ""
    lowest_scorer = ""
    for student in students:
        if student["grade"] == max(s["grade"] for s in students):
            highest_scorer = student["name"]
        if student["grade"] == min(s["grade"] for s in students):
            lowest_scorer = student["name"]
    total_students = len(students)
    class_average = sum(s["grade"] for s in students) / total_students
    passed = sum(1 for s in students if s["grade"] >= 60)
    failed = total_students - passed

    print(f"Total students: {total_students}")
    print(f"Class average: {class_average:.2f}")
    print(f"Highest scorer: {highest_scorer}")
    print(f"Lowest scorer: {lowest_scorer}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")

summarize(students)