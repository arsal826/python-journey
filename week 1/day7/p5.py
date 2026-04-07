sales = [
    {"name": "Arsal",  "region": "north", "amount": 45000},
    {"name": "Ahmed",  "region": "south", "amount": 62000},
    {"name": "Sara",   "region": "north", "amount": 38000},
    {"name": "Ali",    "region": "east",  "amount": 71000},
    {"name": "Zara",   "region": "south", "amount": 55000},
    {"name": "Bob",    "region": "east",  "amount": 48000},
    {"name": "Mia",    "region": "north", "amount": 91000},
    {"name": "John",   "region": "east",  "amount": 33000}
]

# ─────────────────────────────────────
# NOTEBOOK 1 — tracks total sales per region
# starts empty
# after loop: {"north": 174000, "south": 117000, "east": 152000}
# ─────────────────────────────────────
totals = {}

# ─────────────────────────────────────
# NOTEBOOK 2 — tracks how many people per region
# starts empty
# after loop: {"north": 3, "south": 2, "east": 3}
# ─────────────────────────────────────
counts = {}

# ─────────────────────────────────────
# NOTEBOOK 3 — tracks top performer per region
# starts empty
# after loop: {
#   "north": {"name": "Mia",   "amount": 91000},
#   "south": {"name": "Ahmed", "amount": 62000},
#   "east":  {"name": "Ali",   "amount": 71000}
# }
# ─────────────────────────────────────
top = {}

# ─────────────────────────────────────
# MAIN LOOP — go through every sale one by one
# ─────────────────────────────────────
for sale in sales:

    # extract the 3 fields we need
    region = sale["region"]   # "north" "south" or "east"
    amount = sale["amount"]   # 45000, 62000 etc
    name   = sale["name"]     # "Arsal", "Ahmed" etc

    # ─────────────────────────────────
    # FIRST TIME seeing this region?
    # create a fresh page in each notebook
    # ─────────────────────────────────
    if region not in totals:

        # notebook 1 — start total at 0
        # cannot add to something that does not exist
        totals[region] = 0

        # notebook 2 — start count at 0
        counts[region] = 0

        # notebook 3 — assume first person is top performer
        # will update this if someone better comes along
        top[region] = {"name": name, "amount": amount}

    # ─────────────────────────────────
    # ALWAYS runs — every person every region
    # ─────────────────────────────────

    # add this person's amount to region total
    totals[region] += amount

    # one more person in this region
    counts[region] += 1

    # ─────────────────────────────────
    # is this person the top performer?
    # ─────────────────────────────────
    if amount > top[region]["amount"]:
        # yes — update the top performer
        top[region] = {"name": name, "amount": amount}

# ─────────────────────────────────────
# LOOP IS DONE — all employees processed
# now calculate and print results
# ─────────────────────────────────────

# track best region for final summary
best_region = ""
best_total  = 0

for region in totals:

    # calculate average for this region
    avg = totals[region] / counts[region]

    # check if this is the best region so far
    if totals[region] > best_total:
        best_total  = totals[region]
        best_region = region

    # print this region's report
    print(f"\n{region.upper()}")
    print(f"  People:    {counts[region]}")
    print(f"  Total:     {totals[region]}")
    print(f"  Average:   {avg:.2f}")
    print(f"  Top seller:{top[region]['name']} ({top[region]['amount']})")

# print the overall winner
print(f"\nBest region: {best_region.upper()} ({best_total})")
