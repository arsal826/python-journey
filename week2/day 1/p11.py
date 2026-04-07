attendance = [
    {"student": "Arsal",  "date": "2026-01-01", "status": "present"},
    {"student": "Ahmed",  "date": "2026-01-01", "status": "absent"},
    {"student": "Arsal",  "date": "2026-01-02", "status": "present"},
    {"student": "Ahmed",  "date": "2026-01-02", "status": "present"},
    {"student": "Sara",   "date": "2026-01-01", "status": "present"},
    {"student": "Arsal",  "date": "2026-01-03", "status": "absent"},
    {"student": "Ahmed",  "date": "2026-01-03", "status": "present"},
    {"student": "Sara",   "date": "2026-01-02", "status": "absent"},
    {"student": "Sara",   "date": "2026-01-03", "status": "present"},
    {"student": "Arsal",  "date": "2026-01-04", "status": "present"},
]
present_count = {}
absent_count = {}

for record in attendance:
    student = record["student"]
    status = record["status"]

    if student not in present_count:
        present_count[student] = 0
        absent_count[student] = 0

    if status == "present":
        present_count[student] += 1
    else:
        absent_count[student] += 1

average_attendance = {}
for student in present_count:
    total_days = present_count[student] + absent_count[student]
    average_attendance[student] = present_count[student] / total_days if total_days > 0 else 0

max_attendance_student = max(average_attendance, key=average_attendance.get)

student_less_than_70 = []
for student, avg in average_attendance.items():
    if avg < 0.75:
        student_less_than_70.append(student)

print("Average attendance per student:")
for student, avg in average_attendance.items():
    print(f"{student}: {avg:.2%}")
print(f"\nStudent with highest attendance: {max_attendance_student} ({average_attendance[max_attendance_student]:.2%})")
print("\nStudents with attendance less than 70%:")
for student in student_less_than_70:
    print(f"{student}:⚠ Warning - {average_attendance[student]:.2%}")