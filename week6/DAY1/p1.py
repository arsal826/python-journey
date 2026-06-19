products = [
    {"name": "laptop", "price": 50000, "qty": 2},
    {"name": "mouse",  "price": 1500,  "qty": 5},
    {"name": "keyboard","price": 3000, "qty": 3},
]

# Print total value of each product (price × qty)
# Print the grand total of everything
total_value = 0
for product in products:
    product_total = product["price"] * product["qty"]
    total_value += product_total
    print(f"Total value of {product['name']}: {product_total}")

print(f"Grand total: {total_value}")