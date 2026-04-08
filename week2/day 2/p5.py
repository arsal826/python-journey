students = [
    {"name": "Ali",   "subject": "Math",    "marks": 85},
    {"name": "Sara",  "subject": "Math",    "marks": 92},
    {"name": "Ali",   "subject": "Physics", "marks": 78},
    {"name": "Sara",  "subject": "Physics", "marks": 88},
    {"name": "Ahmed", "subject": "Math",    "marks": 70},
    {"name": "Ahmed", "subject": "Physics", "marks": 60},
]

total_marks_per_student = {}
student_counts = {}
subject_totals = {}
subject_counts = {}

# Step 1: Loop once and collect everything
for student in students:
    name = student["name"]
    subject = student["subject"]
    marks = student["marks"]

    # student totals
    if name not in total_marks_per_student:
        total_marks_per_student[name] = 0
        student_counts[name] = 0

    total_marks_per_student[name] += marks
    student_counts[name] += 1

    # subject totals
    if subject not in subject_totals:
        subject_totals[subject] = 0
        subject_counts[subject] = 0

    subject_totals[subject] += marks
    subject_counts[subject] += 1


# Step 2: Calculate averages
average_marks_per_student = {}
for name in total_marks_per_student:
    average_marks_per_student[name] = total_marks_per_student[name] / student_counts[name]


# Step 3: Find top student
highest_total_marks_student = max(total_marks_per_student, key=total_marks_per_student.get)


# Step 4: Find subject with highest average
subject_avg = {}
for sub in subject_totals:
    subject_avg[sub] = subject_totals[sub] / subject_counts[sub]

highest_average_marks_subject = max(subject_avg, key=subject_avg.get)


# Step 5: Print results
print(f"Total marks per student: {total_marks_per_student}")
print(f"Average marks per student: {average_marks_per_student}")
print(f"Student with highest total marks: {highest_total_marks_student}")
print(f"Subject with highest average marks: {highest_average_marks_subject}")


# Step 6: Full report (same style as yours)
for name in total_marks_per_student:
    print(f"\n{name.upper()} REPORT")
    print("-" * 22)

    for student in students:
        if student["name"] == name:
            print(f"{student['subject']:9} → {student['marks']}")

    print(f"Total    → {total_marks_per_student[name]}")
    print(f"Average  → {average_marks_per_student[name]:.1f}")