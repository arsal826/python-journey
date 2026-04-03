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


# # You have:
# scores = {
#     "Arsal": 85,
#     "Ahmed": 92, 
#     "Sara": 67,
#     "Ali": 78,
#     "Zara": 55
# }

# Print a report like this:
# Arsal  → 85 → Pass
# Ahmed  → 92 → Pass
# Sara   → 67 → Pass
# Ali    → 78 → Pass
# Zara   → 55 → Fail

# Then print total passed and total failed

scores = {
    "Arsal": 85,
    "Ahmed": 92, 
    "Sara": 67,
    "Ali": 78,
    "Zara": 55
}
passed = 0
failed = 0
for name, score in scores.items():
    if score >= 60:
        print(f"{name} → {score} → Pass")
        passed += 1
    else:
        print(f"{name} → {score} → Fail")
        failed += 1
print(f"Total passed: {passed}")
print(f"Total failed: {failed}")

# Take this sentence:
# "I am learning Python and Python is amazing and I love Python"
# Find every unique word (no duplicates)
# Print them sorted alphabetically
# Print how many unique words there are

sentence = "I am learning Python and Python is amazing and I love Python"
unique_words = set(sentence.split())
unique_list={}
for word in sorted(unique_words):
    if word in unique_list:
        unique_list[word] += 1
    else:
        unique_list[word] = 1
print(unique_list)

print(f"Total unique words: {len(unique_words)}")

words = sentence.split()
words_count = {}
for word in words:
    if word in words_count:
        words_count[word] += 1
    else:
        words_count[word] = 1

print(words_count)

# Write a function called top_students(students, n)
# It takes a list of student dicts and a number n
# It returns the top n students by grade

# students = [
#     {"name": "Arsal", "grade": 85},
#     {"name": "Ahmed", "grade": 92},
#     {"name": "Sara",  "grade": 67},
#     {"name": "Ali",   "grade": 78},
#     {"name": "Zara",  "grade": 55}
# ]

# top_students(students, 3) should print:
# 1. Ahmed  → 92
# 2. Arsal  → 85
# 3. Ali    → 78

def top_students(students, n):

    # Step 1: sort students (highest grade first)
    sorted_students = sorted(students, key=lambda s: s["grade"], reverse=True)

    # Step 2: print first n students
    for i in range(n):
        student = sorted_students[i]
        print(i + 1, student["name"], "→", student["grade"])

students =[
     {"name": "Arsal", "grade": 85},
     {"name": "Ahmed", "grade": 92},
     {"name": "Sara",  "grade": 67},
     {"name": "Ali",   "grade": 78},
     {"name": "Zara",  "grade": 55}
] 

n=int(input("Enter the number of top students to display: "))
top_students(students, n)
