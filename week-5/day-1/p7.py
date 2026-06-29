transactions = [
    {"user": "Arsal", "type": "credit", "amount": 5000},
    {"user": "Ahmed", "type": "debit",  "amount": 2000},
    {"user": "Arsal", "type": "debit",  "amount": 1500},
    {"user": "Ahmed", "type": "credit", "amount": 8000},
    {"user": "Sara",  "type": "credit", "amount": 3000},
    {"user": "Arsal", "type": "credit", "amount": 2500},
    {"user": "Sara",  "type": "debit",  "amount": 1000},
]

# → Final balance per user (credits - debits)
# → User with highest balance
# → User with most transactions
balances = {}
transaction_counts = {}
for transaction in transactions:
    user = transaction["user"]
    amount = transaction["amount"]
    if user not in balances:
        balances[user] = 0
        transaction_counts[user] = 0
    if transaction["type"] == "credit":
        balances[user] += amount
    else:
        balances[user] -= amount
    transaction_counts[user] += 1

print("Final balances per user:")
for user, balance in balances.items():
    print(f"{user}: {balance}")

highest_balance_user = max(balances, key=balances.get)
print(f"User with highest balance: {highest_balance_user} with a balance of {balances[highest_balance_user]}")

most_transactions_user = max(transaction_counts, key=transaction_counts.get)
print(f"User with most transactions: {most_transactions_user} with {transaction_counts[most_transactions_user]} transactions")