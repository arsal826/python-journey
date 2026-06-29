students = [
    {"name": "Ali",   "score": 85},
    {"name": "Sara",  "score": 92},
    {"name": "Ahmed", "score": 67},
    {"name": "Zara",  "score": 78},
]
total = 0
highest = students[0]
print("Passed Students:")
for student in students:
    if student["score"] >= 70:
        print(student["name"])
    total += student["score"]
    if student["score"] > highest["score"]:
        highest = student

average = total / len(students)
print("Average Score:", average)
print("Highest Scorer:", highest["name"])