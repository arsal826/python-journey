transactions = [
    {"id": "T001", "account": "Ali",   "type": "deposit",    "amount": 50000},
    {"id": "T002", "account": "Sara",  "type": "deposit",    "amount": 30000},
    {"id": "T003", "account": "Ali",   "type": "withdrawal", "amount": 12000},
    {"id": "T004", "account": "Ahmed", "type": "deposit",    "amount": 70000},
    {"id": "T005", "account": "Sara",  "type": "withdrawal", "amount": 5000},
    {"id": "T006", "account": "Ali",   "type": "deposit",    "amount": 20000},
    {"id": "T007", "account": "Ahmed", "type": "withdrawal", "amount": 20000},
    {"id": "T008", "account": "Sara",  "type": "deposit",    "amount": 15000},
]
coustomer_data = {}
transction_count = {}
for transaction in transactions:
    account = transaction["account"]
    t_type = transaction["type"]
    amount = transaction["amount"]

    if account not in coustomer_data:
        coustomer_data[account] = {
            "transactions": [],
            "total_deposits": 0,
            "total_withdrawals": 0,
            "balance": 0,
            "highest_transaction": ("", 0),
            "lowest_transaction": ("", float('inf'))
        }
        transction_count[account] = 0

    coustomer_data[account]["transactions"].append(transaction)
    transction_count[account] += 1
    
    if t_type == "deposit":
        coustomer_data[account]["total_deposits"] += amount
        coustomer_data[account]["balance"] += amount
    elif t_type == "withdrawal":
        coustomer_data[account]["total_withdrawals"] += amount
        coustomer_data[account]["balance"] -= amount
    if amount > coustomer_data[account]["highest_transaction"][1]:
        coustomer_data[account]["highest_transaction"] = (t_type, amount)
    if amount < coustomer_data[account]["lowest_transaction"][1]:
        coustomer_data[account]["lowest_transaction"] = (t_type, amount)

highest_balance_account = max(coustomer_data, key=lambda x: coustomer_data[x]["balance"])
most_transactions_account = max(transction_count, key=transction_count.get)

print(f"Customer with highest balance: {highest_balance_account} (Balance: {coustomer_data[highest_balance_account]['balance']})")
print(f"Customer with most transactions: {most_transactions_account} (Transactions: {transction_count[most_transactions_account]})")
print("\n Highest single transaction:")
for account, data in coustomer_data.items():
    if data["highest_transaction"][1] > 0:
        print(f"{account} → Type: {data['highest_transaction'][0]}, Amount: {data['highest_transaction'][1]}")
print("\n Lowest single transaction:")
for account, data in coustomer_data.items():
    if data["lowest_transaction"][1] < float('inf'):
        print(f"{account} → Type: {data['lowest_transaction'][0]}, Amount: {data['lowest_transaction'][1]}")
print("\nCustomer Details:")
for account, data in coustomer_data.items():
    print(f"\nAccount: {account}")
    print(f"Total Deposits: {data['total_deposits']}")
    print(f"Total Withdrawals: {data['total_withdrawals']}")
    print(f"Balance: {data['balance']}")
    print("Transactions:")
    for transaction in data["transactions"]:
        print(f"  - ID: {transaction['id']}, Type: {transaction['type']}, Amount: {transaction['amount']}")