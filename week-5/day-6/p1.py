data = [
    {"name": "Ali",   "dept": "sales", "amount": 5000},
    {"name": "Sara",  "dept": "tech",  "amount": 8000},
    {"name": "Ahmed", "dept": "sales", "amount": 3000},
    {"name": "Zara",  "dept": "tech",  "amount": 6000},
]

# Total per department
# Highest earner per department
dept_totals = {}
highest_earners = {}

for person in data:
    dept = person["dept"]
    amount = person["amount"]
    name = person["name"]

    # Update total for the department
    if dept in dept_totals:
        dept_totals[dept] += amount
    else:
        dept_totals[dept] = amount

    # Update highest earner for the department
    if dept in highest_earners:
        if amount > highest_earners[dept]["amount"]:
            highest_earners[dept] = person
    else:
        highest_earners[dept] = person

    print(f"Processed {name} from {dept} with amount {amount}")
print("\nTotal Amount per Department:")
for dept, total in dept_totals.items():
    print(f"{dept}: {total}")

print("\nHighest Earner per Department:")
for dept, person in highest_earners.items():
    print(f"{dept}: {person['name']} ({person['amount']})")