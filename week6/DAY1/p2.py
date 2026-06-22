sales = [
    {"seller": "Ali",   "product": "laptop", "amount": 50000},
    {"seller": "Sara",  "product": "phone",  "amount": 30000},
    {"seller": "Ali",   "product": "mouse",  "amount": 2000},
    {"seller": "Ahmed", "product": "laptop", "amount": 48000},
    {"seller": "Sara",  "product": "tablet", "amount": 25000},
    {"seller": "Ali",   "product": "phone",  "amount": 31000},
]

# Total sales per seller
# Seller with highest total sales
# Number of products each seller sold
seller_sales = {}
product_count = {}
for sale in sales:
    seller = sale["seller"]
    amount = sale["amount"]
    product = sale["product"]

    if seller in seller_sales:
        seller_sales[seller] += amount
    else:
        seller_sales[seller] = amount

    if seller in product_count:
        product_count[seller] += 1
    else:
        product_count[seller] = 1

# Find the seller with the highest total sales
highest_seller = max(seller_sales, key=seller_sales.get)
print("Total sales per seller:", seller_sales)
print("Seller with highest total sales:", highest_seller)
print("Number of products each seller sold:", product_count)