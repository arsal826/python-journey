students = [
    {"name": "Ali",   "subject": "Math",    "marks": 85},
    {"name": "Ali",   "subject": "Physics", "marks": 78},
    {"name": "Sara",  "subject": "Math",    "marks": 92},
    {"name": "Sara",  "subject": "Physics", "marks": 88},
]

student_data = {}

for student in students:
    name = student["name"]
    subject = student["subject"]
    marks = student["marks"]

    if name not in student_data:
        student_data[name] = {
            "subjects": {},
            "total": 0,
            "average": 0
        }

    student_data[name]["subjects"][subject] = marks
    student_data[name]["total"] += marks
    total_subjects = len(student_data[name]["subjects"])
    student_data[name]["average"] = student_data[name]["total"] / total_subjects if total_subjects > 0 else 0
    high_achiever = max(student_data, key=lambda x: student_data[x]["average"])

print(student_data)