with open("expenses.txt", "w") as file:
    file.write("food,500\n")
    file.write("transport,200\n")
    file.write("food,300\n")
    file.write("shopping,800\n")
expenses = {}
with open("expenses.txt", "r") as file:
    for line in file:
        category, amount = line.strip().split(",")
        amount = int(amount)
        if category in expenses:
            expenses[category] += amount
        else:
            expenses[category] = amount

print("Total per category:")
for category, total in expenses.items():
    print(f"{category}: {total}")