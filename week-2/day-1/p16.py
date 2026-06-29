medicines = [
    {"name": "Panadol",    "category": "painkiller", "stock": 150, "price": 25,  "sold": 80},
    {"name": "Brufen",     "category": "painkiller", "stock": 200, "price": 45,  "sold": 120},
    {"name": "Flagyl",     "category": "antibiotic", "stock": 80,  "price": 85,  "sold": 60},
    {"name": "Amoxil",     "category": "antibiotic", "stock": 120, "price": 95,  "sold": 90},
    {"name": "Ventolin",   "category": "inhaler",    "stock": 50,  "price": 450, "sold": 35},
    {"name": "Flixotide",  "category": "inhaler",    "stock": 30,  "price": 850, "sold": 28},
    {"name": "ORS",        "category": "supplement", "stock": 300, "price": 15,  "sold": 200},
    {"name": "Vitamin C",  "category": "supplement", "stock": 250, "price": 35,  "sold": 180},
]
total_revenue_per_category = {}
total_remaining_stock_per_category = {}
category_medicines = {}

best_name = ""
max_sold = 0

print("LOW STOCK WARNINGS:")
print("====================")

for medicine in medicines:
    name = medicine["name"]
    category = medicine["category"]
    stock = medicine["stock"]
    price = medicine["price"]
    sold = medicine["sold"]

    revenue = sold * price

    # revenue per category
    if category not in total_revenue_per_category:
        total_revenue_per_category[category] = 0
    total_revenue_per_category[category] += revenue

    # stock per category
    if category not in total_remaining_stock_per_category:
        total_remaining_stock_per_category[category] = 0
    total_remaining_stock_per_category[category] += stock

    # store medicines per category
    if category not in category_medicines:
        category_medicines[category] = []
    category_medicines[category].append(medicine)

    # best seller overall
    if sold > max_sold:
        max_sold = sold
        best_name = name

    # low stock warning
    if stock < 50:
        print(f"{name} → ONLY {stock} LEFT!")

# ---- MOST VALUABLE CATEGORY ----
most_valuable_category = ""
max_revenue = 0
for cat in total_revenue_per_category:
    if total_revenue_per_category[cat] > max_revenue:
        max_revenue = total_revenue_per_category[cat]
        most_valuable_category = cat

# ---- CATEGORY REPORT ----
print("\n=== FULL CATEGORY REPORT ===")

for category in category_medicines:
    print(f"\n{category.upper()}")
    print("=" * 30)

    total_rev = 0
    total_stock = 0
    best_med = ""
    best_sold_cat = 0

    for med in category_medicines[category]:
        name = med["name"]
        stock = med["stock"]
        sold = med["sold"]
        price = med["price"]

        revenue = sold * price
        total_rev += revenue
        total_stock += stock

        if sold > best_sold_cat:
            best_sold_cat = sold
            best_med = name

        print(f"{name:<10} stock:{stock:<5} sold:{sold:<5} revenue:{revenue:,} PKR")

    print("=" * 30)
    print(f"Total revenue: {total_rev:,} PKR")
    print(f"Total stock:   {total_stock}")
    print(f"Best seller:   {best_med} ({best_sold_cat} sold)")

# ---- FINAL SUMMARY ----
print("\n=== SUMMARY ===")
print(f"Best selling medicine overall: {best_name} ({max_sold} sold)")
print(f"Most valuable category: {most_valuable_category} ({max_revenue:,} PKR)")