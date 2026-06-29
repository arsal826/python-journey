orders = [
    {"item": "burger", "price": 500},
    {"item": "fries",  "price": 200},
    {"item": "burger", "price": 500},
    {"item": "cola",   "price": 150},
    {"item": "fries",  "price": 200},
]

# Count how many times each item was ordered
# Print the total revenue
summary={}
for order in orders:
    item = order["item"]
    price = order["price"]

    if item in summary:
        summary[item]["count"] += 1
        summary[item]["revenue"] += price
    else:
        summary[item] = {"count": 1, "revenue": price}

# Print the summary
for item, data in summary.items():
    print(f"{item}: {data['count']} orders, Revenue: {data['revenue']}")
print(f"Total revenue: {sum(data['revenue'] for data in summary.values())}")
