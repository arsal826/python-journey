employees = [
    {"name": "Arsal", "dept": "backend",  "salary": 85000},
    {"name": "Ahmed", "dept": "frontend", "salary": 72000},
    {"name": "Sara",  "dept": "backend",  "salary": 91000},
    {"name": "Ali",   "dept": "frontend", "salary": 68000},
]

# Group by department
# For each department print:
# → Average salary
# → Highest paid person
group= {}
for employee in employees:
    dept = employee["dept"]
    if dept not in group:
        group[dept] = []
    group[dept].append(employee)
for dept, employees in group.items():
    total_salary = sum(employee["salary"] for employee in employees)
    average_salary = total_salary / len(employees)
    
    print(f"Average salary for {dept}: {average_salary:.2f}")
    
    highest_paid = max(employees, key=lambda e: e["salary"])
    print(f"Highest paid in {dept}: {highest_paid['name']} with a salary of {highest_paid['salary']}")