def square(num):
    return num ** 2

def sum_of_squares(a, b):
    return square(a) + square(b)    


a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print(f"The sum of squares of {a} and {b} is {sum_of_squares(a, b)}.")
