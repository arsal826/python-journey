# Write a function called group_by_grade(students)
# It takes a list of students and groups them:

# students = [
#     {"name": "Arsal", "grade": 85},
#     {"name": "Ahmed", "grade": 92},
#     {"name": "Sara",  "grade": 45},
#     {"name": "Ali",   "grade": 78},
#     {"name": "Zara",  "grade": 55},
#     {"name": "Bob",   "grade": 91},
#     {"name": "Mia",   "grade": 63}
# ]

# Group them like this:
# A (90-100): Ahmed, Bob
# B (80-89):  Arsal
# C (70-79):  Ali
# D (60-69):  Mia
# F (below 60): Sara, Zara

# Return a dictionary with grade letters as keys
# and lists of names as values
# Print each group clearly

def group_by_grade(students):
    grade_groups = {"A": [], "B": [], "C": [], "D": [], "F": []}
    for student in students:
        name = student["name"]
        grade = student["grade"]
        if 90 <= grade <= 100:
            grade_groups["A"].append(name)
        elif 80 <= grade < 90:
            grade_groups["B"].append(name)
        elif 70 <= grade < 80:
            grade_groups["C"].append(name)
        elif 60 <= grade < 70:
            grade_groups["D"].append(name)
        else:
            grade_groups["F"].append(name)
    return grade_groups

students = [
    {"name": "Arsal", "grade": 85},
    {"name": "Ahmed", "grade": 92},
    {"name": "Sara",  "grade": 45},
    {"name": "Ali",   "grade": 78},
    {"name": "Zara",  "grade": 55},
    {"name": "Bob",   "grade": 91},
    {"name": "Mia",   "grade": 63}
]

grade_groups = group_by_grade(students)
for grade, names in grade_groups.items():
    print(f"{grade} ({' '.join(names)})")