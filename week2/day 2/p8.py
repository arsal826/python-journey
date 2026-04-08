students = [
    {"name": "Ali", "marks": 85},
    {"name": "Sara", "marks": 92},
    {"name": "Ali", "marks": 78},
    {"name": "Sara", "marks": 88},
]
total_marks_per_student = {}
for student in students:
    name = student["name"]
    marks = student["marks"]

    if name not in total_marks_per_student:
        total_marks_per_student[name] = 0

    total_marks_per_student[name] += marks

highest_total_marks_student = max(total_marks_per_student, key=total_marks_per_student.get)
print(f"Total marks per student: {total_marks_per_student}")
print(f"Student with highest total marks: {highest_total_marks_student} ({total_marks_per_student[highest_total_marks_student]} marks)")
