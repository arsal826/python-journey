# making calculator

while True:
    while True:
        try:
            a=int(input("Enter first number: "))
            b=int(input("Enter second number: "))
            print("The sum is:", a + b)
            break
        except ValueError:
            print("Please enter valid integers.")
    print("enter 1 for addition\n")
    print("enter 2 for subtraction\n")
    print("enter 3 for multiplication\n")
    print("enter 4 for division\n")
    while True:
        try:
            choice=int(input("Enter your choice: "))
            if choice in [1, 2, 3, 4]:
                break
            else:
                print("Please enter a valid choice (1-4).")
        except ValueError:
            print("Please enter a valid choice.")
    if choice == 1:
        print("The sum is:", a + b)
    elif choice == 2:
        print("The difference is:", a - b)
    elif choice == 3:
        print("The product is:", a * b)
    elif choice == 4:
        if b != 0:
            print("The quotient is:", a / b)
        else:
            print("Error: Division by zero is not allowed.")
    cont = input("Do you want to perform another calculation? (yes/no): ").lower().strip()
    if cont != 'yes':
        print("Thank you for using the calculator. Goodbye!")
        break