students = [
    {"name": "Ali",  "grade": 85},
    {"name": "Sara", "grade": 92}
]
result = max(students, key=lambda x: x["grade"])
print(result["name"])
