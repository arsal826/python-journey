# → Total credits
# → Total debits
# → Final balance (credits - debits)
# → Number of transactions each type
# → Largest single transaction and its type
transactions = [
    {"type": "credit", "amount": 5000},
    {"type": "debit",  "amount": 2000},
    {"type": "credit", "amount": 8000},
    {"type": "debit",  "amount": 3500},
    {"type": "credit", "amount": 1500},
    {"type": "debit",  "amount": 4000},
]
transction_summary = {
    "total_credits": 0,
    "total_debits": 0,
    "credit_count": 0,
    "debit_count": 0,
    "final_balance": 0,
    "largest_transaction": {"type": None, "amount": 0}
}
for transaction in transactions:
    if transaction["type"] == "credit":
        transction_summary["total_credits"] += transaction["amount"]
        transction_summary["credit_count"] += 1
    elif transaction["type"] == "debit":
        transction_summary["total_debits"] += transaction["amount"]
        transction_summary["debit_count"] += 1

# Update the largest transaction if the current one is larger
    if transaction["amount"] > transction_summary["largest_transaction"]["amount"]:
        transction_summary["largest_transaction"]["type"] = transaction["type"]
        transction_summary["largest_transaction"]["amount"] = transaction["amount"]

# Calculate the final balance
transction_summary["final_balance"] = transction_summary["total_credits"] - transction_summary["total_debits"]
print(f"Total credits: {transction_summary['total_credits']}")
print(f"Total debits: {transction_summary['total_debits']}")
print(f"Final balance: {transction_summary['final_balance']}")
print(f"Number of credit transactions: {transction_summary['credit_count']}")
print(f"Number of debit transactions: {transction_summary['debit_count']}")
print(f"Largest single transaction: {transction_summary['largest_transaction']['amount']} ({transction_summary['largest_transaction']['type']})")
