# You have:
# orders = [
#     {"customer": "Arsal",  "product": "laptop",  "amount": 150000},
#     {"customer": "Ahmed",  "product": "phone",   "amount": 80000},
#     {"customer": "Arsal",  "product": "earbuds", "amount": 15000},
#     {"customer": "Sara",   "product": "tablet",  "amount": 60000},
#     {"customer": "Ahmed",  "product": "watch",   "amount": 25000},
#     {"customer": "Arsal",  "product": "phone",   "amount": 80000},
#     {"customer": "Sara",   "product": "laptop",  "amount": 150000}
# 
# Calculate per customer:
# → Total amount spent
# → Number of orders
# → Most expensive single purchase
# → List of products they bought

orders = [
    {"customer": "Arsal",  "product": "laptop",  "amount": 150000},
    {"customer": "Ahmed",  "product": "phone",   "amount": 80000},
    {"customer": "Arsal",  "product": "earbuds", "amount": 15000},
    {"customer": "Sara",   "product": "tablet",  "amount": 60000},
    {"customer": "Ahmed",  "product": "watch",   "amount": 25000},      
    {"customer": "Arsal",  "product": "phone",   "amount": 80000},
    {"customer": "Sara",   "product": "laptop",  "amount": 150000}
]

totals    = {}   # {"Arsal": 245000, "Ahmed": 105000, "Sara": 210000}
counts    = {}   # {"Arsal": 3, "Ahmed": 2, "Sara": 2}
expensive = {}   # {"Arsal": 150000, "Ahmed": 80000, "Sara": 150000}
products  = {}   # {"Arsal": ["laptop","earbuds","phone"], ...}

for order in orders:
    customer = order["customer"]
    product  = order["product"]
    amount   = order["amount"]

    if customer not in totals:
        totals[customer] = 0
        counts[customer] = 0
        expensive[customer] = 0
        products[customer] = []

    totals[customer] += amount
    counts[customer] += 1

    if amount > expensive[customer]:
        expensive[customer] = amount

    products[customer].append(product)
for customer in totals:
    print(f"\n{customer.upper()}")
    print(f"  Orders:          {counts[customer]}")
    print(f"  Total spent:     {totals[customer]:,} PKR")
    print(f"  Most expensive:  {expensive[customer]:,} PKR")
    print(f"  Products bought: {', '.join(products[customer])}")
