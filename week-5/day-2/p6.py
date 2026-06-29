products = [
    {"name": "Laptop",  "category": "electronics", "price": 150000, "stock": 5},
    {"name": "Phone",   "category": "electronics", "price": 80000,  "stock": 8},
    {"name": "Shirt",   "category": "clothing",    "price": 2500,   "stock": 50},
    {"name": "Pants",   "category": "clothing",    "price": 3500,   "stock": 30},
    {"name": "Rice",    "category": "food",        "price": 500,    "stock": 100},
    {"name": "Bread",   "category": "food",        "price": 150,    "stock": 200},
]

# Group by category and calculate:
# → Total stock value per category (price × stock)
# → Most expensive item per category
# → Average price per category
# → Category with highest total value
category_data = {}
for product in products:
    category = product["category"]
    price = product["price"]
    stock = product["stock"]
    value = price * stock
    
    if category not in category_data:
        category_data[category] = {
            "total_value": 0,
            "most_expensive": product,
            "total_price": 0,
            "count": 0
        }
    
    category_data[category]["total_value"] += value
    category_data[category]["total_price"] += price
    category_data[category]["count"] += 1
    
    if price > category_data[category]["most_expensive"]["price"]:
        category_data[category]["most_expensive"] = product

# Calculate average price per category
for category, data in category_data.items():
    if data["count"] > 0:
        data["average_price"] = data["total_price"] / data["count"]
    else:
        data["average_price"] = 0

# Find category with highest total value
highest_category = max(category_data, key=lambda k: category_data[k]["total_value"])

print("Category Data:")
for category, data in category_data.items():
    print(f"  {category}:")
    print(f"    Total Value: {data['total_value']}")
    print(f"    Most Expensive: {data['most_expensive']['name']} (${data['most_expensive']['price']})")
    print(f"    Average Price: {data['average_price']:.2f}")

print(f"\nCategory with Highest Total Value: {highest_category}")