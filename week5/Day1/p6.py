# students = [
#     {"name": "Arsal", "grade": 85, "city": "Lahore"},
#     {"name": "Ahmed", "grade": 92, "city": "Karachi"},
#     {"name": "Sara",  "grade": 67, "city": "Lahore"},
#     {"name": "Ali",   "grade": 78, "city": "Karachi"},
# ]
# → Group by city
# → Print average grade per city
# → Print top student per city

students = [
    {"name": "Arsal", "grade": 85, "city": "Lahore"},
    {"name": "Ahmed", "grade": 92, "city": "Karachi"},
    {"name": "Sara",  "grade": 67, "city": "Lahore"},
    {"name": "Ali",   "grade": 78, "city": "Karachi"},
]
group= {}
for student in students:
    city = student["city"]
    if city not in group:
        group[city] = []
    group[city].append(student)
for city, students in group.items():
    total_grade = sum(student["grade"] for student in students)
    average_grade = total_grade / len(students)
    
    print(f"Average grade for {city}: {average_grade:.2f}")
    
    top_student = max(students, key=lambda s: s["grade"])
    print(f"Top student in {city}: {top_student['name']} with a grade of {top_student['grade']}")

