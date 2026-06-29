students = [
    {"name": "Arsal", "city": "Lahore"},
    {"name": "Ahmed", "city": "Karachi"},
    {"name": "Sara", "city": "Lahore"},
    {"name": "Ali", "city": "Karachi"},
    {"name": "Usman", "city": "Lahore"},
]

group = {}

for student in students:
    city = student["city"]
    if city not in group:
        group[city] = []
    group[city].append(student)

for city, city_students in group.items():
    names = [s["name"] for s in city_students]
    print(f"{city}: {names}")
    print(f"{city}: {len(city_students)} students")

most_students_city = max(group, key=lambda c: len(group[c]))
print(f"\nCity with most students: {most_students_city} ({len(group[most_students_city])})")