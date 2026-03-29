def get_postive(prompt):
    while True:
        try:
            num = int(input(prompt))
            if num > 0:
                return num
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
def calculate_sum(num1, num2):
    return num1 + num2
def calculate_product(num1, num2):
    return num1 * num2
history = []
while True:
    while True:
        num1 = get_postive("Enter the first positive integer: ")
        num2 = get_postive("Enter the second positive integer: ")
        break  
    choice= input("Choose an operation + for sum, * for product: ")
    if choice == '+':
        result = calculate_sum(num1, num2)
        print(f"The sum of {num1} and {num2} is: {result}")
        history.append(f"{num1} + {num2} = {result}")      
    elif choice == '*':
        result = calculate_product(num1, num2)
        print(f"The product of {num1} and {num2} is: {result}")
        history.append(f"{num1} * {num2} = {result}")
    cont=input("do you want to continue? (yes/no): ").lower()
    if cont != 'yes':
        print("History of calculations:")
        for record in history:
            print(record)
        break