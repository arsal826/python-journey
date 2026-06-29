students = [
    {"name": "Ali",   "grade": 85, "city": "Lahore"},
    {"name": "Sara",  "grade": 92, "city": "Karachi"},
    {"name": "Ahmed", "grade": 78, "city": "Lahore"},
    {"name": "Zara",  "grade": 65, "city": "Karachi"},
    {"name": "Bob",   "grade": 91, "city": "Islamabad"}
]
# Group students by city
# For each city print:
# → Students in that city
# → Average grade of that city
# → Top student in that city

city_data = {}
for student in students:
    city = student["city"]
    grade = student["grade"]
    name = student["name"]

    if city not in city_data:
        city_data[city] = {
            "students": [],
            "total_grade": 0,
            "top_student": {"name": "", "grade": 0}
        }

    city_data[city]["students"].append(name)
    city_data[city]["total_grade"] += grade

    if grade > city_data[city]["top_student"]["grade"]:
        city_data[city]["top_student"] = {"name": name, "grade": grade}
for city, data in city_data.items():
    average_grade = data["total_grade"] / len(data["students"])
    print(f"City: {city}")
    print(f"Students: {', '.join(data['students'])}")
    print(f"Average Grade: {average_grade:.2f}")
    print(f"Top Student: {data['top_student']['name']} (Grade: {data['top_student']['grade']})")
    print()