# expenses = [
#     {"date": "2026-01-05", "category": "food",      "amount": 2500},
#     {"date": "2026-01-12", "category": "transport",  "amount": 800},
#     {"date": "2026-02-03", "category": "food",      "amount": 3200},
#     {"date": "2026-02-14", "category": "shopping",  "amount": 5500},
#     {"date": "2026-01-20", "category": "food",      "amount": 1800},
#     {"date": "2026-02-25", "category": "transport",  "amount": 600},
#     {"date": "2026-03-01", "category": "food",      "amount": 2900},
#     {"date": "2026-03-15", "category": "shopping",  "amount": 3200},
#     {"date": "2026-01-28", "category": "transport",  "amount": 1200},
#     {"date": "2026-03-22", "category": "food",      "amount": 1500}
# ]
# ```

# Calculate and print:
# ```
# → Total spent per category
# → Total spent per month
# → Most expensive month
# → Most expensive category
# → Average expense per transaction
# → All transactions above 2000 PKR

expenses = [
    {"date": "2026-01-05", "category": "food",      "amount": 2500},
    {"date": "2026-01-12", "category": "transport",  "amount": 800},
    {"date": "2026-02-03", "category": "food",      "amount": 3200},
    {"date": "2026-02-14", "category": "shopping",  "amount": 5500},
    {"date": "2026-01-20", "category": "food",      "amount": 1800},
    {"date": "2026-02-25", "category": "transport",  "amount": 600},
    {"date": "2026-03-01", "category": "food",      "amount": 2900},
    {"date": "2026-03-15", "category": "shopping",  "amount": 3200},
    {"date": "2026-01-28", "category": "transport",  "amount": 1200},
    {"date": "2026-03-22", "category": "food",      "amount": 1500}
]  
total_per_category = {}
total_per_month = {}
average_expense = 0
above_2000 = []
for expense in expenses:
    category = expense["category"]
    amount = expense["amount"]
    month = expense["date"][:7]  # Extract YYYY-MM

    # Total spent per category
    if category in total_per_category:
        total_per_category[category] += amount
    else:
        total_per_category[category] = amount

    # Total spent per month
    if month in total_per_month:
        total_per_month[month] += amount
    else:
        total_per_month[month] = amount

    # Average expense per transaction
    average_expense += amount

    # All transactions above 2000 PKR
    if amount > 2000:
        above_2000.append(expense)
average_expense /= len(expenses)
# Most expensive month
most_expensive_month = max(total_per_month, key=total_per_month.get)
# Most expensive category
most_expensive_category = max(total_per_category, key=total_per_category.get)
# Print results
print("Total spent per category:")
for category, total in total_per_category.items():
    print(f"  {category}: {total} PKR")
print("\nTotal spent per month:")
for month, total in total_per_month.items():
    print(f"  {month}: {total} PKR")
print(f"\nMost expensive month: {most_expensive_month} ({total_per_month[most_expensive_month]} PKR)")
print(f"Most expensive category: {most_expensive_category} ({total_per_category[most_expensive_category]} PKR)")
print(f"\nAverage expense per transaction: {average_expense:.2f} PKR")
print("\nTransactions above 2000 PKR:")