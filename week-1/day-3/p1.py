 #Write a function called greet(name) that prints 'Hello name, welcome!'
def function(name):
    print(f"Hello, {name}!")    


name = input("Enter your name: ")
function(name)  
 
 
 #Write a function that squares a number and returns the result'
def square(num):
    return num ** 2

number = float(input("Enter a number: "))
result = square(number)
print(f"The square of {number} is {result}.")


#Write a function called is_even(n) that returns True if even, False if odd

def is_even(n):
    return n % 2 == 0
number = int(input("Enter a number: "))
if is_even(number):
    print(f"{number} is even.") 
else:
    print(f"{number} is odd.") 

#Write a function called celsius_to_fahrenheit(c) that returns the converted value
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius}°C is equal to {fahrenheit}°F.")


#Call each function and print the results
print(function(name))   
print(square(number))
print(is_even(number))
print(celsius_to_fahrenheit(celsius))