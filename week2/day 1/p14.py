# Bookstore orders
orders = [
    {"customer": "Ali",  "book": "Python 101",   "quantity": 1, "price": 500},
    {"customer": "Sara", "book": "Python 101",   "quantity": 2, "price": 450},
    {"customer": "Ali",  "book": "Data Science", "quantity": 1, "price": 1200},
    {"customer": "Zara", "book": "Python 101",   "quantity": 1, "price": 500},
    {"customer": "Ali",  "book": "Python 101",   "quantity": 1, "price": 450},  # discounted
]

# Dictionaries to store metrics
revenue_per_book = {}
copies_per_book = {}
customer_orders = {}
total_spent_per_customer = {}

# Process each order
for order in orders:
    customer = order["customer"]
    book = order["book"]
    quantity = order["quantity"]
    price = order["price"]

    # ---- revenue per book ----
    if book not in revenue_per_book:
        revenue_per_book[book] = 0
    revenue_per_book[book] += quantity * price

    # ---- total copies sold per book ----
    if book not in copies_per_book:
        copies_per_book[book] = 0
    copies_per_book[book] += quantity

    # ---- store orders per customer ----
    if customer not in customer_orders:
        customer_orders[customer] = []
    customer_orders[customer].append({
        "book": book,
        "quantity": quantity,
        "price": price
    })

    # ---- total spending per customer ----
    if customer not in total_spent_per_customer:
        total_spent_per_customer[customer] = 0
    total_spent_per_customer[customer] += quantity * price

# ---- most popular book ----
most_popular_book = ""
highest_quantity = 0
for book in copies_per_book:
    if copies_per_book[book] > highest_quantity:
        highest_quantity = copies_per_book[book]
        most_popular_book = book

# ---- customer who bought most books ----
most_books_customer = ""
max_books = 0
for customer in customer_orders:
    total_books = 0
    for o in customer_orders[customer]:
        total_books += o["quantity"]
    if total_books > max_books:
        max_books = total_books
        most_books_customer = customer

# ---- PRINT SUMMARY ----
print("=== Total Revenue per Book ===")
for book in revenue_per_book:
    print(f"{book}: {revenue_per_book[book]:,} PKR")

print("\n=== Total Copies Sold per Book ===")
for book in copies_per_book:
    print(f"{book}: {copies_per_book[book]} copies")

print(f"\nMost popular book: {most_popular_book} ({highest_quantity} copies sold)")
print(f"Customer who bought most books: {most_books_customer} ({max_books} books)")

# ---- Detailed invoice per customer ----
print("\n=== Detailed Invoices per Customer ===")
for customer in customer_orders:
    print(f"\n{customer}:")
    total_customer = 0
    # Aggregate repeated books with same price
    book_summary = {}
    for o in customer_orders[customer]:
        key = (o["book"], o["price"])
        if key not in book_summary:
            book_summary[key] = 0
        book_summary[key] += o["quantity"]

    # Print invoice lines
    for (book, price), qty in book_summary.items():
        line_total = price * qty
        total_customer += line_total
        print(f"  {book} x{qty} @ {price:,} → {line_total:,} PKR")
    print(f"  Total → {total_customer:,} PKR")