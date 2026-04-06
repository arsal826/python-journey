overtime = [
    {"employee": "Ali",    "week": 1, "hours": 5},
    {"employee": "Sara",   "week": 1, "hours": 8},
    {"employee": "Ali",    "week": 2, "hours": 6},
    {"employee": "Sara",   "week": 2, "hours": 4},
    {"employee": "Ahmed",  "week": 1, "hours": 7},
    {"employee": "Ahmed",  "week": 2, "hours": 5},
    {"employee": "Ali",    "week": 3, "hours": 4},
    {"employee": "Sara",   "week": 3, "hours": 6}
]
total_employee_hours = {}
total_week_hours = {}
employee_more_than_6 = []
for entry in overtime:
    employee = entry["employee"]
    week = entry["week"]
    hours = entry["hours"]

    if employee not in total_employee_hours:
        total_employee_hours[employee] = 0
    if week not in total_week_hours:
        total_week_hours[week] = 0
    
    # Total hours per employee
    if employee in total_employee_hours:
        total_employee_hours[employee] += hours
    else:
        total_employee_hours[employee] = hours

    # Total hours per week
    if week in total_week_hours:
        total_week_hours[week] += hours
    else:
        total_week_hours[week] = hours

    # Employees who worked more than 6 hours in a week
    if hours > 6:
        employee_more_than_6.append((employee, week, hours))
# Employee with highest overtime
max_employee = max(total_employee_hours, key=total_employee_hours.get)
# Week with highest overtime
max_week = max(total_week_hours, key=total_week_hours.get)
print("Total hours per employee:")
for employee, hours in total_employee_hours.items():
    print(f"{employee}: {hours} hours")
print("\nTotal hours per week:")
for week, hours in total_week_hours.items():
    print(f"Week {week}: {hours} hours")
print(f"\nEmployee with highest overtime: {max_employee} ({total_employee_hours[max_employee]} hours)")
print(f"Week with highest overtime: Week {max_week} ({total_week_hours[max_week]} hours)")
print("\nEmployees who worked more than 6 hours in a week:")
for employee, week, hours in employee_more_than_6:
    print(f"{employee} worked {hours} hours in Week {week}")    