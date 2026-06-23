sales = [
    {"rep": "Ali",   "region": "north", "amount": 5000, "month": "Jan"},
    {"rep": "Sara",  "region": "south", "amount": 8000, "month": "Jan"},
    {"rep": "Ali",   "region": "north", "amount": 6000, "month": "Feb"},
    {"rep": "Ahmed", "region": "south", "amount": 4000, "month": "Jan"},
    {"rep": "Sara",  "region": "south", "amount": 9000, "month": "Feb"},
    {"rep": "Ali",   "region": "north", "amount": 7000, "month": "Feb"},
]

# Total sales per region
# Total sales per month
# Best performing rep (highest total)

sales_region = {}
sales_month = {}
sales_rep = {}

for sale in sales:
    region = sale["region"]
    month = sale["month"]
    rep = sale["rep"]
    amount = sale["amount"]

    sales_region[region] = sales_region.get(region, 0) + amount
    sales_month[month] = sales_month.get(month, 0) + amount
    sales_rep[rep] = sales_rep.get(rep, 0) + amount

best_rep = max(sales_rep, key=sales_rep.get)

print("Sales by region:", sales_region)
print("Sales by month:", sales_month)
print("Sales by rep:", sales_rep)
print("Best performing rep:", best_rep, "-", sales_rep[best_rep])