orders = [
    {"product": "Apple", "quantity": 10},
    {"product": "Banana", "quantity": 5},
    {"product": "Apple", "quantity": 7},
    {"product": "Orange", "quantity": 3},
    {"product": "Banana", "quantity": 2},
]
total_sales_per_product = {}
for order in orders:
    product = order["product"]
    quantity = order["quantity"]

    if product not in total_sales_per_product:
        total_sales_per_product[product] = 0

    total_sales_per_product[product] += quantity
print(total_sales_per_product)
