expenses = [
    {"category": "food",      "amount": 500},
    {"category": "transport", "amount": 200},
    {"category": "food",      "amount": 300},
    {"category": "shopping",  "amount": 800},
]

# Total per category
category_totals = {}
for expense in expenses:
    category = expense["category"]
    amount = expense["amount"]

    if category not in category_totals:
        category_totals[category] = 0

    category_totals[category] += amount