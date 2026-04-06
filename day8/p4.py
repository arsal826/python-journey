def invoice(orders, customer_name):
    filtered = []

    # Step 1: filter orders
    for order in orders:
        if order["customer"] == customer_name:
            filtered.append(order)

    # Step 2: check if empty
    if len(filtered) == 0:
        print("Customer not found")
        return

    # Step 3: heading
    print("INVOICE FOR:", customer_name)
    print("=" * 30)

    total_amount = 0

    # Step 4: print orders
    count = 1
    for order in filtered:
        print(f"{count}. {order['product']:<10} → {order['amount']:>10,} PKR")
        total_amount += order["amount"]
        count += 1

    # Step 5: totals
    total_orders = len(filtered)
    average = total_amount // total_orders

    print("=" * 30)
    print("Total orders:", total_orders)
    print("Total amount:", format(total_amount, ","), "PKR")
    print("Average order:", format(average, ","), "PKR")
    print("=" * 30)

orders = [
    {"customer": "Arsal",  "product": "laptop",  "amount": 150000},
    {"customer": "Ahmed",  "product": "phone",   "amount": 80000},
    {"customer": "Arsal",  "product": "earbuds", "amount": 15000},
    {"customer": "Sara",   "product": "tablet",  "amount": 60000},
    {"customer": "Ahmed",  "product": "watch",   "amount": 25000},
    {"customer": "Arsal",  "product": "phone",   "amount": 80000},
    {"customer": "Sara",   "product": "laptop",  "amount": 150000}
    ]
invoice(orders, "Arsal")
print()
invoice(orders, "Ahmed")
print()
invoice(orders, "Zara")
