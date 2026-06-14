sales = [
    {"product": "laptop", "category": "tech", "amount": 50000},
    {"product": "shirt",  "category": "wear", "amount": 2000},
    {"product": "phone",  "category": "tech", "amount": 30000},
    {"product": "pants",  "category": "wear", "amount": 3000},
]

# Group by category
# Print total amount per category

category_data = {}
for sale in sales:
    category = sale["category"]
    amount = sale["amount"]

    if category not in category_data:
        category_data[category] = 0

    category_data[category] += amount

for category, total in category_data.items():
    print(f"{category}: {total}")