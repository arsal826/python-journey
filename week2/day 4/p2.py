sales = [
    {"id": "S001", "customer": "Ali",   "book": "Python Basics", "quantity": 2, "price": 500},
    {"id": "S002", "customer": "Sara",  "book": "Learn Java",    "quantity": 1, "price": 600},
    {"id": "S003", "customer": "Ali",   "book": "Python Basics", "quantity": 1, "price": 500},
    {"id": "S004", "customer": "Ahmed", "book": "Data Science",  "quantity": 3, "price": 700},
    {"id": "S005", "customer": "Sara",  "book": "Python Basics", "quantity": 2, "price": 500},
    {"id": "S006", "customer": "Ali",   "book": "Learn Java",    "quantity": 1, "price": 600},
]
customer_data = {}
best_selling_book = {}
for sale in sales:
    customer = sale["customer"]
    book = sale["book"]
    quantity = sale["quantity"]
    total_price = sale["quantity"] * sale["price"]

    if customer not in customer_data:
        customer_data[customer] = {
            "purchases": [],
            "total_spent": 0,
            "most_expensive_book": ("", 0),
            "least_expensive_book": ("", float('inf')),
            "average_spent": 0,
            "book_counts":{},
            "book_spending":{},
        }
    if book not in best_selling_book:
        best_selling_book[book] = 0
    if book not in customer_data[customer]["book_counts"]:
        customer_data[customer]["book_counts"][book] = 0
        customer_data[customer]["book_spending"][book] = 0
    
    customer_data[customer]["purchases"].append(sale)
    total_price = quantity * sale["price"]
    customer_data[customer]["total_spent"] += total_price
    customer_data[customer]["book_counts"][book] += quantity
    customer_data[customer]["book_spending"][book] += total_price
    best_selling_book[book] += quantity

    if total_price > customer_data[customer]["most_expensive_book"][1]:
        customer_data[customer]["most_expensive_book"] = (book, total_price)
    if total_price < customer_data[customer]["least_expensive_book"][1]:
        customer_data[customer]["least_expensive_book"] = (book, total_price)
    
for customer, data in customer_data.items():
    total_purchases = len(data["purchases"])
    data["average_spent"] = data["total_spent"] / total_purchases if total_purchases > 0 else 0
    customer_data[customer]["most_bought_book"] = max(data["book_counts"], key=data["book_counts"].get)
    customer_data[customer]["most_spent_book"] = max(data["book_spending"], key=data["book_spending"].get)
best_selling = max(best_selling_book, key=best_selling_book.get)
highest_spent_customer = max(customer_data, key=lambda x: customer_data[x]["total_spent"])
most_purchases_customer = max(customer_data, key=lambda x: len(customer_data[x]["purchases"]))
loyal_customer = max(customer_data, key=lambda x: len(customer_data[x]["book_counts"]))
print("\nCustomer Details:")
for customer, data in customer_data.items():
    print(f"\nCustomer: {customer}")
    print(f"Purchases:")
    for purchase in data["purchases"]:
        print(f"  - ID: {purchase['id']}, Book: {purchase['book']}, Quantity: {purchase['quantity']}, Price: {purchase['price']}")
    print(f"Total Spent: {data['total_spent']}")
    print(f"Average Spent: {data['average_spent']:.2f}")
    print(f"Most Expensive Book: {data['most_expensive_book'][0]} (Total Price: {data['most_expensive_book'][1]})")
    print(f"Least Expensive Book: {data['least_expensive_book'][0]} (Total Price: {data['least_expensive_book'][1]})")
    print(f"Most Bought Book: {data['most_bought_book']}")
    print(f"Most Spent Book: {data['most_spent_book']}")
print(f"\nBest Selling Book: {best_selling} (Total Quantity Sold: {best_selling_book[best_selling]})")
print(f"Customer with Highest Spending: {highest_spent_customer} (Total Spent: {customer_data[highest_spent_customer]['total_spent']})")
print(f"Customer with Most Purchases: {most_purchases_customer} (Total Purchases: {len(customer_data[most_purchases_customer]['purchases'])})")
print(f"Loyal Customer: {loyal_customer} (Unique Books Bought: {len(customer_data[loyal_customer]['book_counts'])})")
