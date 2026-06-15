# One expense as a dictionary
expense = {"category": "food", "amount": 500}

# Save it to a file as: food,500
with open("expenses.txt", "w") as f:
    line = expense["category"] + "," + str(expense["amount"])
    f.write(line + "\n")

print("Saved!")

# Read the file
with open("expenses.txt", "r") as f:
    line = f.readline()        # reads "food,500\n"
    line = line.strip()        # removes \n → "food,500"
    parts = line.split(",")    # splits → ["food", "500"]
    
    # rebuild the dictionary
    expense = {
        "category": parts[0],        # "food"
        "amount": int(parts[1])      # 500 — convert back to number!
    }

print(expense)
print(f"Category: {expense['category']}")
print(f"Amount: {expense['amount']}")