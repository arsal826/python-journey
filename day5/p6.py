# Take this list of students:
#     students = [
#         {"name": "Arsal", "grade": 85},
#         {"name": "Ahmed", "grade": 92},
#         {"name": "Sara",  "grade": 67},
#         {"name": "Ali",   "grade": 78}
#     ]
#     Print only students with grade above 80
#     Print the class average
#     Print the highest scoring student's name

students = {
    "Arsal": 85,
    "Ahmed": 92,
    "Sara": 67,
    "Ali": 78
}

# Print only students with grade above 80
hight_achiever = []
for student, grade in students.items():
    if grade > 80:
        hight_achiever.append(student)
print("Students with grade above 80:", hight_achiever)

# Print the class average
total_grade = sum(students.values())
class_average = total_grade / len(students)
print(f"Class average: {class_average}")

# Print the highest scoring student's name
for student, grade in students.items():
    if grade == max(students.values()):
        print(f"Highest scoring student: {student}")

students = [
    {"name": "Arsal", "grade": 85},
    {"name": "Ahmed", "grade": 92},
    {"name": "Sara",  "grade": 67},
    {"name": "Ali",   "grade": 78}
]

# find highest scoring student's name
# without using max()
# just a loop and a variable to track winner
winner = students[0]
winner_list = []
for student in students:
    if student["grade"] > winner["grade"]:
        winner = student
        winner_list.append(student)
print(f"Highest scoring student: {winner['name']}")
print("All students who had the highest grade and their marks are:", [(student["name"], student["grade"]) for student in winner_list])