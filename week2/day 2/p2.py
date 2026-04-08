# → Total completed revenue
# → Total returned amount
# → Return rate percentage
# → Customer with most returns
# → Most returned product
# → Net revenue (completed - returned)
# → Per customer report:
#   Arsal → completed: 1  returned: 2  net: -95,000 PKR
#   Ahmed → completed: 2  returned: 1  net:  65,000 PKR
#   Sara  → completed: 2  returned: 0  net: 210,000 PKR

transactions = [
    {"order_id": "A001", "customer": "Arsal", "product": "laptop",  "amount": 150000, "status": "completed"},
    {"order_id": "A002", "customer": "Ahmed", "product": "phone",   "amount": 80000,  "status": "returned"},
    {"order_id": "A003", "customer": "Sara",  "product": "tablet",  "amount": 60000,  "status": "completed"},
    {"order_id": "A004", "customer": "Arsal", "product": "earbuds", "amount": 15000,  "status": "returned"},
    {"order_id": "A005", "customer": "Ahmed", "product": "watch",   "amount": 25000,  "status": "completed"},
    {"order_id": "A006", "customer": "Sara",  "product": "laptop",  "amount": 150000, "status": "completed"},
    {"order_id": "A007", "customer": "Arsal", "product": "phone",   "amount": 80000,  "status": "returned"},
    {"order_id": "A008", "customer": "Ahmed", "product": "tablet",  "amount": 60000,  "status": "completed"},
]

# Initialize variables
total_completed_revenue = 0
total_returned_amount = 0
customer_returns = {}
product_returns = {}

if not transactions:
    print("No transactions available.")

for transaction in transactions:
    if transaction["status"] == "completed":
        total_completed_revenue += transaction["amount"]
    elif transaction["status"] == "returned":
        total_returned_amount += transaction["amount"]
        customer_returns[transaction["customer"]] = customer_returns.get(transaction["customer"], 0) + 1
        product_returns[transaction["product"]] = product_returns.get(transaction["product"], 0) + 1

return_rate_percentage = (total_returned_amount / total_completed_revenue * 100) if total_completed_revenue > 0 else 0
most_returned_customer = max(customer_returns, key=customer_returns.get) if customer_returns else None
most_returned_product = max(product_returns, key=product_returns.get) if product_returns else None
net_revenue = total_completed_revenue - total_returned_amount

print(f"Total completed revenue: {total_completed_revenue}")
print(f"Total returned amount: {total_returned_amount}")
print(f"Return rate percentage: {return_rate_percentage:.2f}%")
print(f"Customer with most returns: {most_returned_customer} ({customer_returns.get(most_returned_customer, 0)} returns)")
print(f"Most returned product: {most_returned_product} ({product_returns.get(most_returned_product, 0)} returns)")
print(f"Net revenue: {net_revenue}")

for customer in ["Arsal", "Ahmed", "Sara"]:
    completed = sum(1 for t in transactions if t["customer"] == customer and t["status"] == "completed")
    returned = sum(1 for t in transactions if t["customer"] == customer and t["status"] == "returned")
    net = sum(t["amount"] for t in transactions if t["customer"] == customer and t["status"] == "completed") - sum(t["amount"] for t in transactions if t["customer"] == customer and t["status"] == "returned")
    print(f"{customer} → completed: {completed}  returned: {returned}  net: {net:+,} PKR")

