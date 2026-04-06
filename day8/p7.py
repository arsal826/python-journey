sales = [
    {"date": "2026-01-01", "product": "Shirt",  "amount": 1500},
    {"date": "2026-01-02", "product": "Pant",   "amount": 2200},
    {"date": "2026-01-03", "product": "Shirt",  "amount": 1800},
    {"date": "2026-01-04", "product": "Shoes",  "amount": 3200},
    {"date": "2026-01-05", "product": "Pant",   "amount": 2000},
    {"date": "2026-01-06", "product": "Shirt",  "amount": 2700},
    {"date": "2026-01-07", "product": "Shoes",  "amount": 1500}
]

total_per_product = {}
total_per_day = {}
max_product = ""
product_above_2000 = []
max_day = ""
for sale in sales:
    product = sale["product"]
    amount = sale["amount"]
    date = sale["date"]

    # Total sales per product
    if product in total_per_product:
        total_per_product[product] += amount
    else:
        total_per_product[product] = amount

    # Total sales per day
    if date in total_per_day:
        total_per_day[date] += amount
    else:
        total_per_day[date] = amount
    
    # Sales above 2000
    if amount > 2000:
        product_above_2000.append(sale)

    # Product with highest sales
max_product = max(total_per_product, key=total_per_product.get)
    # Day with highest sales
max_day = max(total_per_day, key=total_per_day.get)
