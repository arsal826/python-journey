orders = [
    {"table": 1, "item": "burger", "price": 850, "qty": 2},
    {"table": 1, "item": "fries",  "price": 350, "qty": 3},
    {"table": 1, "item": "cola",   "price": 150, "qty": 2},
    {"table": 2, "item": "pizza",  "price": 1200, "qty": 1},
    {"table": 2, "item": "cola",   "price": 150, "qty": 2},
    {"table": 3, "item": "burger", "price": 850, "qty": 1},
    {"table": 3, "item": "fries",  "price": 350, "qty": 1},
    {"table": 3, "item": "cola",   "price": 150, "qty": 1},
]

total_per_table = {}
item_per_table = {}
items_all_tables = {}

for order in orders:
    table = order["table"]
    item = order["item"]
    price = order["price"]
    qty = order["qty"]

    # ---- initialize ----
    if table not in total_per_table:
        total_per_table[table] = 0
        item_per_table[table] = {}

    # ---- total per table ----
    total_per_table[table] += price * qty

    # ---- items per table (UPDATED STRUCTURE) ----
    if item in item_per_table[table]:
        item_per_table[table][item]["qty"] += qty
    else:
        item_per_table[table][item] = {"qty": qty, "price": price}

    # ---- global item count ----
    if item in items_all_tables:
        items_all_tables[item] += qty
    else:
        items_all_tables[item] = qty


# ---- MOST ORDERED ITEM ----
most_ordered_item = max(items_all_tables, key=items_all_tables.get)

# ---- TABLE WITH HIGHEST BILL ----
table_highest_bill = max(total_per_table, key=total_per_table.get)


# ---- PRINT SUMMARY ----
print("Total bill per table:")
for table, total in total_per_table.items():
    print(f"Table {table}: {total:,} PKR")

print(f"\nMost ordered item: {most_ordered_item} (Quantity: {items_all_tables[most_ordered_item]})")
print(f"Table with highest bill: {table_highest_bill} (Bill: {total_per_table[table_highest_bill]:,} PKR)")


# ---- PRINT BILL PER TABLE ----
for table, items in item_per_table.items():
    print(f"\nTABLE {table} BILL")
    print("=" * 25)

    for item, details in items.items():
        qty = details["qty"]
        price = details["price"]
        total = qty * price   # calculate here (better design)

        print(f"{item.ljust(10)} x{qty} → {total:>6,} PKR")

    print("=" * 25)
    print(f"Total:      → {total_per_table[table]:>6,} PKR")