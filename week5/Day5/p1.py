records = [
    {"name": "Ali",   "dept": "sales", "amount": 50000},
    {"name": "Sara",  "dept": "tech",  "amount": 30000},
    {"name": "Ahmed", "dept": "sales", "amount": 70000},
    {"name": "Zara",  "dept": "tech",  "amount": 40000},
]

# Total amount per department
totals = {}
for record in records:
    dept = record["dept"]
    amount = record["amount"]
    if dept in totals:
        totals[dept] += amount
    else:
        totals[dept] = amount
print(totals)
# Average amount per department
averages = {}
for dept, total in totals.items():
    count = sum(1 for record in records if record["dept"] == dept)
    averages[dept] = total / count
print(averages)