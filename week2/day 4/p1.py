orders = [
    {"id": "O001", "customer": "Ali",   "product": "Laptop", "amount": 120000},
    {"id": "O002", "customer": "Sara",  "product": "Phone",  "amount": 80000},
    {"id": "O003", "customer": "Ali",   "product": "Mouse",  "amount": 2000},
    {"id": "O004", "customer": "Ahmed", "product": "Laptop", "amount": 115000},
    {"id": "O005", "customer": "Sara",  "product": "Mouse",  "amount": 2500},
    {"id": "O006", "customer": "Ali",   "product": "Phone",  "amount": 75000},
    {"id": "O007", "customer": "Ahmed", "product": "Mouse",  "amount": 1500},
]
customer_data = {}
product_sales = {}
for order in orders:
    customer = order["customer"]
    product = order["product"]
    amount = order["amount"]

    if customer not in customer_data:
        customer_data[customer] = {
            "orders": [],
            "total_spent": 0,
            "highest_order": ("", 0),
            "lowest_order": ("", float('inf')),
            "average_order": 0,
            "product_counts":{},
            "product_spending":{},
        }
    if product not in product_sales:
        product_sales[product] = 0
    if product not in customer_data[customer]["product_counts"]:
        customer_data[customer]["product_counts"][product] = 0
        customer_data[customer]["product_spending"][product] = 0
    
    customer_data[customer]["orders"].append(order)
    customer_data[customer]["total_spent"] += amount
    customer_data[customer]["product_counts"][product] += 1
    customer_data[customer]["product_spending"][product] += amount
    product_sales[product] += amount
    

    if amount > customer_data[customer]["highest_order"][1]:
        customer_data[customer]["highest_order"] = (product, amount)
    if amount < customer_data[customer]["lowest_order"][1]:
        customer_data[customer]["lowest_order"] = (product, amount)
for customer, data in customer_data.items():
    data["average_order"] = data["total_spent"] / len(data["orders"])
    customer_data[customer]["most_bought_product"] = max(data["product_counts"], key=data["product_counts"].get)
    customer_data[customer]["most_spent_product"] = max(data["product_spending"], key=data["product_spending"].get)

best_product = max(product_sales, key=product_sales.get)
highest_spent_customer = max(customer_data, key=lambda x: customer_data[x]["total_spent"])
most_orders_customer = max(customer_data, key=lambda x: len(customer_data[x]["orders"]))
loyal_customer = max(customer_data, key=lambda x: len(customer_data[x]["product_counts"]))

print("\nCustomer Details:")
for customer, data in customer_data.items():
    print(f"\nCustomer: {customer}")
    print(f"orders:")
    for order in data["orders"]:
        print(f"  - ID: {order['id']}, Product: {order['product']}, Amount: {order['amount']}")
    print(f"Total Spent: {data['total_spent']}")
    print(f"Average Order Value: {data['average_order']:.2f}")
    print(f"Highest Order: Product: {data['highest_order'][0]}, Amount: {data['highest_order'][1]}")
    print(f"Lowest Order: Product: {data['lowest_order'][0]}, Amount: {data['lowest_order'][1]}")
    print(f"Most Bought Product: {data['most_bought_product']}")
    print(f"Most Spent Product: {data['most_spent_product']}")

print(f"\nLoyal Customer: {loyal_customer} (Unique Products Bought: {len(customer_data[loyal_customer]['product_counts'])})")
print(f"\nmost sold product: {best_product} with total sales of {product_sales[best_product]}")
print(f"Customer with highest total spent: {highest_spent_customer} (Total Spent: {customer_data[highest_spent_customer]['total_spent']})")
print(f"Customer with most orders: {most_orders_customer} (Orders: {len(customer_data[most_orders_customer]['orders'])})")
