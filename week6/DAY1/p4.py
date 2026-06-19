employees = [
    {"name": "Ali",   "dept": "sales", "salary": 50000, "years": 3},
    {"name": "Sara",  "dept": "tech",  "salary": 80000, "years": 5},
    {"name": "Ahmed", "dept": "sales", "salary": 45000, "years": 2},
    {"name": "Zara",  "dept": "tech",  "salary": 90000, "years": 6},
    {"name": "Bob",   "dept": "sales", "salary": 55000, "years": 4},
    {"name": "Mia",   "dept": "tech",  "salary": 70000, "years": 1},
]

# For each department:
# → average salary
# → most experienced employee (highest years)
# Also: give everyone with 4+ years a 10% raise
#       and print their new salary
dept_data = {}
for emp in employees:
    dept = emp["dept"]
    salary = emp["salary"]
    years = emp["years"]

    if dept not in dept_data:
        dept_data[dept] = {"total_salary": 0, "count": 0, "most_exp": None}

    dept_data[dept]["total_salary"] += salary
    dept_data[dept]["count"] += 1

    if (dept_data[dept]["most_exp"] is None or 
        years > dept_data[dept]["most_exp"]["years"]):
        dept_data[dept]["most_exp"] = emp

# Calculate average salary for each department
for dept, data in dept_data.items():
    avg_salary = data["total_salary"] / data["count"] if data["count"] > 0 else 0
    print(f"{dept.capitalize()}: Average Salary = {avg_salary:.2f}")

# Print the most experienced employee in each department
for dept, data in dept_data.items():
    if data["most_exp"]:
        print(f"{dept.capitalize()}: Most Experienced Employee = {data['most_exp']['name']} with {data['most_exp']['years']} years")

# Give everyone with 4+ years a 10% raise and print their new salary
for emp in employees:
    if emp["years"] >= 4:
        emp["salary"] *= 1.1
        print(f"{emp['name']}: New Salary = {emp['salary']:.2f}")