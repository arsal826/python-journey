def function_1():
    print("This is function 1")

function_1()


def function_2(x):  
    return x * 2    

number = int(input("Enter a number: "))    
result = function_2(number)
print(result)   


def function_3(x, y):  
    return x + y    


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))  
result = function_3(num1, num2)
print("The sum is:", result)   