def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("Error: Division by zero is undefined.")
        return None
    return a / b


history = []

while True:
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            break
        except ValueError:
            print("Invalid input. Please enter numeric values.")

    sign = input("Choose operation: + - * / : ")

    if sign == '+':
        result = add(num1, num2)
    elif sign == '-':
        result = subtract(num1, num2)
    elif sign == '*':
        result = multiply(num1, num2)
    elif sign == '/':
        result = divide(num1, num2)
    else:
        print("Invalid operation. Please enter +, -, *, or /.")
        continue

    if result is not None:
        calculation = f"{num1} {sign} {num2} = {result}"
        print("Result:", result)
        history.append(calculation)

    choice = input("Do you want to calculate again? (yes/no): ").lower()
    if choice != "yes":
        break

print("\nCalculation History:")
for item in history:
    print(item)