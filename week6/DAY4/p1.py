inventory = [
    {"product": "laptop", "category": "tech",  "stock": 5,  "price": 50000},
    {"product": "shirt",  "category": "wear",  "stock": 20, "price": 1500},
    {"product": "phone",  "category": "tech",  "stock": 8,  "price": 30000},
    {"product": "jeans",  "category": "wear",  "stock": 15, "price": 3000},
]

# Total stock value per category (stock × price, summed)
# Category with the most total value
category_values = {}
for item in inventory:
    category = item["category"]
    total_value = item["stock"] * item["price"]
    if category in category_values:
        category_values[category] += total_value
    else:
        category_values[category] = total_value

most_valuable_category = max(category_values, key=category_values.get)
print("Total stock value per category:", category_values)
print("Category with the most total value:", most_valuable_category)