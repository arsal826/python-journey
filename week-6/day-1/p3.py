transactions = [
    {"user": "Ali",   "type": "credit", "amount": 5000},
    {"user": "Sara",  "type": "debit",  "amount": 2000},
    {"user": "Ali",   "type": "debit",  "amount": 1500},
    {"user": "Sara",  "type": "credit", "amount": 8000},
    {"user": "Ali",   "type": "credit", "amount": 3000},
    {"user": "Ahmed", "type": "credit", "amount": 6000},
    {"user": "Sara",  "type": "debit",  "amount": 1000},
]

# For each user calculate:
# → total credits
# → total debits
# → final balance (credits - debits)
# Print who has the highest balance
user_data = {}
for transaction in transactions:
    user = transaction["user"]
    t_type = transaction["type"]
    amount = transaction["amount"]

    if user not in user_data:
        user_data[user] = {"credit": 0, "debit": 0}

    if t_type == "credit":
        user_data[user]["credit"] += amount
    elif t_type == "debit":
        user_data[user]["debit"] += amount

# Calculate final balances and find the user with the highest balance
highest_user = None
highest_balance = float('-inf')

for user, data in user_data.items():
    balance = data["credit"] - data["debit"]
    print(f"{user}: Credits = {data['credit']}, Debits = {data['debit']}, Balance = {balance}")

    if balance > highest_balance:
        highest_balance = balance
        highest_user = user

print(f"\nUser with the highest balance: {highest_user} with a balance of {highest_balance}")
