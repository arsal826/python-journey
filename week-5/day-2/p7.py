results = [
    {"name": "Arsal", "subject": "Math",    "score": 85},
    {"name": "Arsal", "subject": "Science", "score": 92},
    {"name": "Arsal", "subject": "English", "score": 78},
    {"name": "Ahmed", "subject": "Math",    "score": 72},
    {"name": "Ahmed", "subject": "Science", "score": 68},
    {"name": "Ahmed", "subject": "English", "score": 85},
    {"name": "Sara",  "subject": "Math",    "score": 95},
    {"name": "Sara",  "subject": "Science", "score": 88},
    {"name": "Sara",  "subject": "English", "score": 91},
]

student_data = {}

# Group by student
for result in results:
    name = result["name"]
    subject = result["subject"]
    score = result["score"]

    if name not in student_data:
        student_data[name] = {
            "total_score": 0,
            "count": 0,
            "best_subject": subject,
            "worst_subject": subject,
            "best_score": score,
            "worst_score": score
        }

    student_data[name]["total_score"] += score
    student_data[name]["count"] += 1

    if score > student_data[name]["best_score"]:
        student_data[name]["best_score"] = score
        student_data[name]["best_subject"] = subject

    if score < student_data[name]["worst_score"]:
        student_data[name]["worst_score"] = score
        student_data[name]["worst_subject"] = subject

# Calculate averages
for name, data in student_data.items():
    data["average_score"] = data["total_score"] / data["count"]

# Find highest and second-highest average students
sorted_students = sorted(
    student_data.items(),
    key=lambda x: x[1]["average_score"],
    reverse=True
)

highest_student = sorted_students[0][0]
second_highest_student = sorted_students[1][0]

# Find best student per subject
best_per_subject = {}

for result in results:
    subject = result["subject"]
    name = result["name"]
    score = result["score"]

    if subject not in best_per_subject:
        best_per_subject[subject] = {
            "name": name,
            "score": score
        }
    elif score > best_per_subject[subject]["score"]:
        best_per_subject[subject]["name"] = name
        best_per_subject[subject]["score"] = score

# Output
print("Student Data:")
for name, data in student_data.items():
    print(f"\n{name}:")
    print(f"  Average Score: {data['average_score']:.2f}")
    print(f"  Best Subject: {data['best_subject']} ({data['best_score']})")
    print(f"  Worst Subject: {data['worst_subject']} ({data['worst_score']})")

print("\nStudent with Highest Overall Average:", highest_student)
print("Student with Second Highest Overall Average:", second_highest_student)

print("\nBest Student Per Subject:")
for subject, data in best_per_subject.items():
    print(f"{subject}: {data['name']} ({data['score']})")