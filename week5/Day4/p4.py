def add_expenses():
    category = input("Enter expense category: ")
    amount = int(input("Enter expense amount: "))
    with open("expenses.txt", "a") as f:
        line = category + "," + str(amount)
        f.write(line + "\n")

def view_expenses():
    with open("expenses.txt", "r") as f:
        for line in f:
            parts = line.strip().split(",")
            category = parts[0]
            amount = parts[1]
            print(f"{category}: {amount}")

def total_expenses():
    total = 0
    with open("expenses.txt", "r") as f:
        for line in f:
            parts = line.strip().split(",")
            amount = int(parts[1])
            total += amount
    print("Total expenses:", total)

while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Exit")
    choice = input("Choose an option: ")
    
    if choice == "1":
        add_expenses()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expenses()
    elif choice == "4":
        break
    else:
        print("Invalid option, please try again.")