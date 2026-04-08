students = [
    {"name": "Ali",   "subject": "Math",    "marks": 85},
    {"name": "Ali",   "subject": "Physics", "marks": 78},
    {"name": "Ali",   "subject": "Chemistry","marks": 92},
    {"name": "Sara",  "subject": "Math",    "marks": 92},
    {"name": "Sara",  "subject": "Physics", "marks": 88},
    {"name": "Sara",  "subject": "Chemistry","marks": 81},
]

student_data = {}
subject_totals = {}
subject_counts = {}

# Collect data
for student in students:
    name = student["name"]
    subject = student["subject"]
    marks = student["marks"]

    if name not in student_data:
        student_data[name] = {
            "subjects": {},
            "total": 0,
            "average": 0,
            "HIGH ACHIEVER": False
        }

    if subject not in subject_totals:
        subject_totals[subject] = 0
        subject_counts[subject] = 0

    student_data[name]["subjects"][subject] = marks
    student_data[name]["total"] += marks
    subject_totals[subject] += marks
    subject_counts[subject] += 1

# Calculate averages for each student
for name in student_data:
    total_subjects = len(student_data[name]["subjects"])
    student_data[name]["average"] = student_data[name]["total"] / total_subjects if total_subjects > 0 else 0

# Mark high achiever
high_achiever = max(student_data, key=lambda x: student_data[x]["average"])
student_data[high_achiever]["HIGH ACHIEVER"] = True

# Calculate highest average subject
highest_avg_subject = max(subject_totals, key=lambda x: subject_totals[x]/subject_counts[x])

# Print report
print(f"Highest Average Subject: {highest_avg_subject}\n")
for name, data in student_data.items():
    print(f"{name.upper()} REPORT")
    print("-" * 30)
    for subject, marks in data["subjects"].items():
        print(f"{subject:10} → {marks}")
    print(f"Total   → {data['total']}")
    print(f"Average → {data['average']:.2f}")
    if data["HIGH ACHIEVER"]:
        print("🏆 HIGH ACHIEVER")
    print()