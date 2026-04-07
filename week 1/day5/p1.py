#Store operation history
history = []

def add(x, y):
    return x + y

def add_to_history(operation, x, y, result):
        history.append(f"{operation}: {x} {operation} {y} = {result}")

def show_history():
        if not history:
            print("No history yet")
        else:
            print("\nCalculation History:")
            for entry in history:
                print(entry)

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y

def calculator():
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    choice = input("Enter operation (1/2/3/4): ")
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    result = None
    operation = None
    if choice == '1':
        result = add(num1, num2)
        operation = "Add"
        print(f"Result: {result}")
    elif choice == '2':
        result = subtract(num1, num2)
        operation = "Subtract"
        print(f"Result: {result}")
    elif choice == '3':
        result = multiply(num1, num2)
        operation = "Multiply"
        print(f"Result: {result}")
    elif choice == '4':
        result = divide(num1, num2)
        operation = "Divide"
        print(f"Result: {result}")
    else:
        print("Invalid choice")
    
    if result is not None and operation is not None:
        add_to_history(operation, num1, num2, result)

# Run calculator
calculator()
show_history()