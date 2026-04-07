# → Current balance per account (deposits - withdrawals)
# → Total deposits per account
# → Total withdrawals per account
# → Account with highest balance
# → Account with most transactions
# → Any account with balance below 30000 → print warning
# → Full statement per account:

# ARSAL ACCOUNT STATEMENT
# ================================
# T001  deposit     +50,000 PKR
# T003  withdrawal  -15,000 PKR
# T006  deposit     +25,000 PKR
# T009  withdrawal   -8,000 PKR
# ================================
# Balance: 52,000 PKR # → Current balance per account (deposits - withdrawals)
# # → Total deposits per account
# # → Total withdrawals per account
# # → Account with highest balance
# # → Account with most transactions
# # → Any account with balance below 30000 → print warning
# # → Full statement per account:

# # ARSAL ACCOUNT STATEMENT
# # ================================
# # T001  deposit     +50,000 PKR
# # T003  withdrawal  -15,000 PKR
# # T006  deposit     +25,000 PKR
# # T009  withdrawal   -8,000 PKR
# # ================================
# # Balance: 52,000 PKR
transactions = [
    {"id": "T001", "account": "Arsal", "type": "deposit",    "amount": 50000},
    {"id": "T002", "account": "Ahmed", "type": "deposit",    "amount": 30000},
    {"id": "T003", "account": "Arsal", "type": "withdrawal", "amount": 15000},
    {"id": "T004", "account": "Sara",  "type": "deposit",    "amount": 80000},
    {"id": "T005", "account": "Ahmed", "type": "withdrawal", "amount": 10000},
    {"id": "T006", "account": "Arsal", "type": "deposit",    "amount": 25000},
    {"id": "T007", "account": "Sara",  "type": "withdrawal", "amount": 30000},
    {"id": "T008", "account": "Ahmed", "type": "deposit",    "amount": 45000},
    {"id": "T009", "account": "Arsal", "type": "withdrawal", "amount": 8000},
    {"id": "T010", "account": "Sara",  "type": "deposit",    "amount": 20000},
]
current_balance = {}
total_deposits = {}
total_withdrawals = {}
account_less_than_30000 = []
account_transactions_count = {}
for transaction in transactions:
    account = transaction["account"]
    t_type = transaction["type"]
    amount = transaction["amount"]

    if account not in current_balance:
        current_balance[account] = 0
        total_deposits[account] = 0
        total_withdrawals[account] = 0
        account_transactions_count[account] = 0

    if t_type == "deposit":
        current_balance[account] += amount
        total_deposits[account] += amount
    elif t_type == "withdrawal":
        current_balance[account] -= amount
        total_withdrawals[account] += amount

    account_transactions_count[account] += 1

for account, balance in current_balance.items():
    if balance < 30000:
        account_less_than_30000.append(account)

highest_balance_account = max(current_balance, key=current_balance.get)
most_transactions_account = max(account_transactions_count, key=account_transactions_count.get)
print(f"Current balance per account: {current_balance}")
print(f"Total deposits per account: {total_deposits}")
print(f"Total withdrawals per account: {total_withdrawals}")
print(f"Account with highest balance: {highest_balance_account} ({current_balance[highest_balance_account]} PKR)")
print(f"Account with most transactions: {most_transactions_account} ({account_transactions_count[most_transactions_account]} transactions)")
if account_less_than_30000:
    print(f"Warning: The following accounts have balance below 30,000 PKR: {', '.join(account_less_than_30000)}")
for account in current_balance:
    print(f"\n{account.upper()} ACCOUNT STATEMENT")
    print("=" * 30)
    for transaction in transactions:
        if transaction["account"] == account:
            t_id = transaction["id"]
            t_type = transaction["type"]
            amount = transaction["amount"]
            sign = "+" if t_type == "deposit" else "-"
            print(f"{t_id}  {t_type:11} {sign}{amount:,} PKR")
    print("=" * 30)
    print(f"Balance: {current_balance[account]:,} PKR")
    