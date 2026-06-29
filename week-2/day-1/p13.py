orders = [
    {"customer": "Ali",    "product": "Laptop",      "quantity": 1, "price": 120000},
    {"customer": "Sara",   "product": "Mouse",       "quantity": 2, "price": 1500},
    {"customer": "Ali",    "product": "Mouse",       "quantity": 1, "price": 1600},
    {"customer": "Zara",   "product": "Keyboard",    "quantity": 1, "price": 3000},
    {"customer": "Sara",   "product": "Laptop",      "quantity": 1, "price": 115000},
    {"customer": "Ali",    "product": "Keyboard",    "quantity": 1, "price": 2800},
    {"customer": "Zara",   "product": "Mouse",       "quantity": 3, "price": 1400},
    {"customer": "Ali",    "product": "Laptop",      "quantity": 1, "price": 118000},  # discounted
]

# Dictionaries to store metrics
revenue_per_product = {}
quantity_per_product = {}
spending_per_customer = {}
customer_orders = {}  # list of orders per customer

# Process each order
for o in orders:
    customer = o["customer"]
    product = o["product"]
    quantity = o["quantity"]
    price = o["price"]

    # ---- revenue per product ----
    if product not in revenue_per_product:
        revenue_per_product[product] = 0
    revenue_per_product[product] += quantity * price

    # ---- quantity sold per product ----
    if product not in quantity_per_product:
        quantity_per_product[product] = 0
    quantity_per_product[product] += quantity

    # ---- spending per customer ----
    if customer not in spending_per_customer:
        spending_per_customer[customer] = 0
    spending_per_customer[customer] += quantity * price

    # ---- store orders per customer ----
    if customer not in customer_orders:
        customer_orders[customer] = []
    customer_orders[customer].append({
        "product": product,
        "quantity": quantity,
        "price": price
    })

# ---- MOST SOLD PRODUCT ----
most_sold_product = max(quantity_per_product, key=lambda k: quantity_per_product[k])

# ---- HIGHEST REVENUE PRODUCT ----
highest_revenue_product = max(revenue_per_product, key=lambda k: revenue_per_product[k])

# ---- HIGHEST SPENDING CUSTOMER ----
highest_spending_customer = max(spending_per_customer, key=lambda k: spending_per_customer[k])

# ---- PRINT SUMMARY ----
print("=== Total revenue per product ===")
for product in sorted(revenue_per_product):
    print(f"{product}: ${revenue_per_product[product]:,}")

print(f"\nMost sold product: {most_sold_product} ({quantity_per_product[most_sold_product]} units)")
print(f"Highest revenue product: {highest_revenue_product} (${revenue_per_product[highest_revenue_product]:,})")
print(f"Highest spending customer: {highest_spending_customer} (${spending_per_customer[highest_spending_customer]:,})")

# ---- DETAILED INVOICE PER CUSTOMER ----
print("\n=== Detailed Invoices per Customer ===")
for customer, orders_list in customer_orders.items():
    print(f"\n{customer}:")
    total_customer = 0
    # Aggregate repeated products at different prices
    product_summary = {}
    for order in orders_list:
        key = (order["product"], order["price"])  # track separately if price differs
        if key not in product_summary:
            product_summary[key] = 0
        product_summary[key] += order["quantity"]

    # Print invoice
    for (product, price), qty in product_summary.items():
        line_total = price * qty
        total_customer += line_total
        print(f"  {product} x{qty} @ {price:,} → {line_total:,} PKR")
    print(f"  Total → {total_customer:,} PKR")