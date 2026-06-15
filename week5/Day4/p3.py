expenses = [
    {"category": "food",      "amount": 500},
    {"category": "transport", "amount": 200},
    {"category": "shopping",  "amount": 800},
]
with open("expenses.txt", "w") as f:
    for expense in expenses:
        line = expense["category"] + "," + str(expense["amount"])
        f.write(line + "\n")
print("Saved!")

total=0
with open("expenses.txt", "r") as f:
    for line in f:
        line=line.strip()
        parts=line.split(",")
        category=parts[0]
        amount=int(parts[1])
        total+=amount
print("Total expenses:", total)