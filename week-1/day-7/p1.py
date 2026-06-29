# Take this string:
# "arsal:23:lahore:backend-developer"

# Split by colon to get each piece
# Then create a dictionary from it:
# {
#   "name": "arsal",
#   "age": 23,
#   "city": "lahore", 
#   "profession": "backend-developer"
# }
# Print each key and value
data = "arsal:23:lahore:backend-developer"

keys = ["name", "age", "city", "profession"]
values = data.split(":")

result = dict(zip(keys, values))
result["age"] = int(result["age"])

for key, value in result.items():
    print(key, ":", value)

# You have two lists:
# students_a = ["Arsal", "Ahmed", "Sara", "Ali"]
# students_b = ["Sara", "Ali", "Zara", "Bob"]

# Find:
# → Students in BOTH classes
# → Students in class A but NOT in class B
# → Students in class B but NOT in class A
# → All students combined with no duplicates

# No using set()

students_a = ["Arsal", "Ahmed", "Sara", "Ali"]
students_b = ["Sara", "Ali", "Zara", "Bob"]
both_classes = []
only_a = []
only_b = []
all_students = []
for student in students_a:
    if student in students_b:
        both_classes.append(student)
    else:
        only_a.append(student)

for student in students_b:
    if student not in students_a:
        only_b.append(student)
# Add all from A
for student in students_a:
    if student not in all_students:
        all_students.append(student)

# Add from B only if not already present
for student in students_b:
    if student not in all_students:
        all_students.append(student)

print("All:", all_students)
print("Students in both classes:", both_classes)
print("Students in class A but not in class B:", only_a)
print("Students in class B but not in class A:", only_b)
