orders = [
    {"customer": "Arsal", "amount": 5000},
    {"customer": "Ahmed", "amount": 3000},
    {"customer": "Arsal", "amount": 2000},
    {"customer": "Sara",  "amount": 8000},
    {"customer": "Ahmed", "amount": 4000},
]
# → Total per customer
# → Highest spending customer
# Total per customer
totals = {}
for order in orders:
    customer = order["customer"]
    amount = order["amount"]
    if customer in totals:
        totals[customer] += amount
    else:
        totals[customer] = amount

# Highest spending customer
highest_customer = max(totals, key=totals.get)
print("Total per customer:", totals)
print("Highest spending customer:", highest_customer)
