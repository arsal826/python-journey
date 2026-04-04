employees = [
    {"name": "Arsal",  "dept": "backend",  "salary": 85000},
    {"name": "Ahmed",  "dept": "frontend", "salary": 72000},
    {"name": "Sara",   "dept": "backend",  "salary": 91000},
    {"name": "Ali",    "dept": "frontend", "salary": 68000},
    {"name": "Zara",   "dept": "backend",  "salary": 78000},
    {"name": "Bob",    "dept": "frontend", "salary": 95000}
]

# Step 1 — create empty tracking dictionaries
# think of these as empty notebooks
dept_salaries = {}   # will store: {"backend": 254000, "frontend": 235000}
dept_counts   = {}   # will store: {"backend": 3, "frontend": 3}
dept_highest  = {}   # will store: {"backend": Sara, "frontend": Bob}
dept_lowest =  {}   # single number, tracks company total
second_largest = {}
total_salary  = 0 
# Step 2 — loop through every employee
for emp in employees:
    
    # extract the two fields we need
    dept   = emp["dept"]     # "backend" or "frontend"
    salary = emp["salary"]   # 85000, 72000 etc

    # add to company total — always, every employee
    total_salary += salary

    # Step 3 — first time we see this department?
    if dept not in dept_salaries:
        # YES — never seen this dept before
        # create a fresh entry for it
        dept_salaries[dept] = 0    # start salary total at 0
        dept_counts[dept]   = 0    # start people count at 0
        dept_highest[dept]  = emp  # assume first person is highest
        dept_lowest[dept] = emp
        second_largest[dept] = emp

    # Step 4 — update the dept totals
    # runs every time, not just first time
    dept_salaries[dept] += salary  # add this salary to dept total
    dept_counts[dept]   += 1       # one more person in this dept

    # Step 5 — is this person the highest paid in their dept?
    if salary > dept_highest[dept]["salary"]:
        second_largest[dept] = dept_highest[dept]  # yes — update the second highest before updating the winner
        dept_highest[dept] = emp  # yes — update the winner
    if salary > second_largest[dept]["salary"] and salary != dept_highest[dept]["salary"]:
        second_largest[dept] = emp
    
    if salary < dept_lowest[dept]["salary"]:
        dept_lowest[dept] = emp   # yes — update the lowest

# Step 6 — all employees processed, now print results
print("=" * 40)
for dept in dept_salaries:
    
    # calculate average for this dept
    avg = dept_salaries[dept] / dept_counts[dept]
    
    print(f"\nDepartment: {dept.upper()}")
    print(f"  Employees:       {dept_counts[dept]}")
    print(f"  Total salary:    {dept_salaries[dept]}")
    print(f"  Average salary:  {avg:.2f}")
    print(f"  Highest paid:    {dept_highest[dept]['name']} ({dept_highest[dept]['salary']})")
    print(f"  Lowest paid:     {dept_lowest[dept]['name']} ({dept_lowest[dept]['salary']})")
    print(f"  Second highest:  {second_largest[dept]['name']} ({second_largest[dept]['salary']})")

print("=" * 40)
print(f"\nTotal company salary budget: {total_salary}")
