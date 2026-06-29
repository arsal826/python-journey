orders = [
    {"customer": "Ali", "product": "Apple",     "quantity": 5, "price": 100,  "category": "fruits"},
    {"customer": "Sara","product": "Milk",      "quantity": 2, "price": 80,   "category": "dairy"},
    {"customer": "Ali", "product": "Apple",     "quantity": 3, "price": 90,   "category": "fruits"}, # discount
    {"customer": "Zara","product": "Carrot",    "quantity": 4, "price": 50,   "category": "vegetables"},
    {"customer": "Sara","product": "Apple",     "quantity": 2, "price": 100,  "category": "fruits"},
    {"customer": "Ali", "product": "Milk",      "quantity": 1, "price": 85,   "category": "dairy"},
]
# --- Dictionary Names for Grocery Orders Analysis ---

# 1. Total revenue per product
# Key: product name
# Value: total revenue (quantity × price)
revenue_per_product = {}

# 2. Total quantity sold per product
# Key: product name
# Value: total quantity sold
quantity_per_product = {}

# 3. Total revenue per category
# Key: category name (e.g., "fruits", "dairy")
# Value: total revenue for all products in that category
revenue_per_category = {}

# 4. Customer orders (for spending and invoices)
# Key: customer name
# Value: list of order dictionaries containing:
#        "product", "quantity", "price", "category"
customer_orders = {}

# 5. Total spending per customer (optional, can be calculated from customer_orders)
# Key: customer name
# Value: total amount spent
total_spent_per_customer = {}

for order in orders:
    customer = order["customer"]
    product = order["product"]
    quantity = order["quantity"]
    price = order["price"]
    category = order["category"]

    # ---- revenue per product ----
    if product not in revenue_per_product:
        revenue_per_product[product] = 0
    revenue_per_product[product] += quantity * price

    # ---- quantity sold per product ----
    if product not in quantity_per_product:
        quantity_per_product[product] = 0
    quantity_per_product[product] += quantity

    # ---- revenue per category ----
    if category not in revenue_per_category:
        revenue_per_category[category] = 0
    revenue_per_category[category] += quantity * price

    # ---- store orders per customer ----
    if customer not in customer_orders:
        customer_orders[customer] = []
    customer_orders[customer].append({
        "product": product,
        "quantity": quantity,
        "price": price,
        "category": category
    })

    # ---- total spending per customer (optional) ----
    if customer not in total_spent_per_customer:
        total_spent_per_customer[customer] = 0
    total_spent_per_customer[customer] += quantity * price

# ---- MOST SOLD PRODUCT ----
most_sold_product = max(quantity_per_product, key=lambda k: quantity_per_product[k])    
# ---- HIGHEST REVENUE PRODUCT ----
highest_revenue_product = max(revenue_per_product, key=lambda k: revenue_per_product[k])
# ---- HIGHEST REVENUE CATEGORY ----
highest_revenue_category = max(revenue_per_category, key=lambda k: revenue_per_category[k])
# ---- HIGHEST SPENDING CUSTOMER ----
highest_spending_customer = max(total_spent_per_customer, key=lambda k: total_spent_per_customer[k])
# ---- PRINT SUMMARY ----
print("=== Total revenue per product ===")
for product in sorted(revenue_per_product):
    print(f"{product}: ${revenue_per_product[product]:,}")
print("\n=== Total revenue per category ===")
for category in sorted(revenue_per_category):
    print(f"{category.capitalize()}: ${revenue_per_category[category]:,}")
print(f"\nMost sold product: {most_sold_product} ({quantity_per_product[most_sold_product]} units)")
print(f"Highest revenue product: {highest_revenue_product} (${revenue_per_product[highest_revenue_product]:,})")
print(f"Highest revenue category: {highest_revenue_category.capitalize()} (${revenue_per_category[highest_revenue_category]:,})")
print(f"Highest spending customer: {highest_spending_customer} (${total_spent_per_customer[highest_spending_customer]:,})")
# ---- DETAILED INVOICE PER CUSTOMER ----
print("\n=== Detailed Invoices per Customer ===")
for customer, orders_list in customer_orders.items():
    print(f"\n{customer}:")
    total_customer = 0
    for o in orders_list:
        product = o["product"]
        quantity = o["quantity"]
        price = o["price"]
        category = o["category"]
        total = quantity * price
        total_customer += total
        print(f"  - {product} ({category}): {quantity} × ${price} = ${total:,}")
    print(f"  Total: ${total_customer:,}")
    