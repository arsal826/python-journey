

# Calculate and print:
# ```
# → Total bill per table (price × qty)
# → Number of items ordered per table
# → Most ordered item across all tables
# → Table with highest bill
# → Print a bill for each table like this:

# TABLE 1 BILL
# ========================
# burger  x2  →  1,700 PKR
# fries   x3  →  1,050 PKR
# cola    x2  →    300 PKR
# ========================
# # Total:      →  3,050 

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

    if table not in total_per_table:
        total_per_table[table] = 0
        item_per_table[table] = {}

    total_per_table[table] += price * qty

    if item in item_per_table[table]:
        item_per_table[table][item]["qty"] += qty
        item_per_table[table][item]["total"] += price * qty
    else:
        item_per_table[table][item] = {"qty": qty, "total": price * qty}

    if item in items_all_tables:
        items_all_tables[item] += qty
    else:
        items_all_tables[item] = qty
most_ordered_item = max(items_all_tables, key=items_all_tables.get)
table_highest_bill = max(total_per_table, key=total_per_table.get)
print("Total bill per table:")
for table, total in total_per_table.items():
    print(f"Table {table}: {total} PKR")

print(f"Most ordered item: {most_ordered_item} (Quantity: {items_all_tables[most_ordered_item]})")
print(f"Table with highest bill: {table_highest_bill} (Bill: {total_per_table[table_highest_bill]} PKR)")
for table, items in item_per_table.items():
    print(f"\nTABLE {table} BILL")
    print("=" * 30)
    for item, details in items.items():
        print(f"{item.ljust(10)} x{details['qty']} → {details['total']:,} PKR")
    print("=" * 30)
    print(f"Total: {' ' * 12} → {total_per_table[table]:,} PKR")
