# Calculate and print:
# ```
# → Total sales per region
# → Average sales per region
# → Top performer in each region (highest amount)
# → Which region made the most total sales
# → How many salespeople in each region

sales= [
    {"name": "Arsal",  "region": "north", "amount": 45000},
    {"name": "Ahmed",  "region": "south", "amount": 62000},
    {"name": "Sara",   "region": "north", "amount": 38000},
    {"name": "Ali",    "region": "east",  "amount": 71000},
    {"name": "Zara",   "region": "south", "amount": 55000},
    {"name": "Bob",    "region": "east",  "amount": 48000},
    {"name": "Mia",    "region": "north", "amount": 91000},
    {"name": "John",   "region": "east",  "amount": 33000}
]
sales_counts = {}
sales_totals = {}
sales_top = {}
salespeople_counts = {}
second_largest = {}
second_lowest = {}
for sale in sales:
    region = sale["region"]
    amount = sale["amount"]
    name = sale["name"]

    if region not in sales_counts:
        sales_counts[region] = 0
        sales_totals[region] = 0
        sales_top[region] = {"name": name, "amount": amount}
        salespeople_counts[region] = 0
        second_largest[region] = {"name": None, "amount": float('-inf')}
        second_lowest[region] = {"name": None, "amount": float('inf')}

    sales_counts[region] += 1
    sales_totals[region] += amount
    salespeople_counts[region] += 1

    if amount > sales_top[region]["amount"]:
        sales_top[region] = {"name": name, "amount": amount}
    if amount > second_largest[region]["amount"] and amount != sales_top[region]["amount"]:
        second_largest[region] = {"name": name, "amount": amount}
    if amount < second_lowest[region]["amount"] and amount != sales_top[region]["amount"]:
        second_lowest[region] = {"name": name, "amount": amount}
for region in sales_counts:
    total = sales_totals[region]
    count = sales_counts[region]
    avg = total / count
    top_performer = sales_top[region]
    second_performer = second_largest[region]
    lowest_performer = second_lowest[region]
    print(f"Region: {region}")
    print(f"  Total Sales: {total}")
    print(f"  Average Sales: {avg:.2f}")
    print(f"  Top Performer: {top_performer['name']} ({top_performer['amount']})")
    print(f"  Second Performer: {second_performer['name']} ({second_performer['amount']})")
    print(f"  Lowest Performer: {lowest_performer['name']} ({lowest_performer['amount']})")