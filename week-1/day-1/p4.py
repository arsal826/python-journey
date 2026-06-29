#      ask the user to imagine a number.
  #Set a variable: number = 17
  #Print whether it is:
   # even or odd (hint: use %)
   #greater than 10 or not
   # both even AND greater than 10

number = 17     
number = 17

if number % 2 == 0 and number > 10:
    print("Even AND greater than 10")
elif number % 2 != 0 and number > 10:
    print("Odd but still greater than 10")
elif number % 2 == 0 and number <= 10:
    print("Even but not greater than 10")
else:
    print("Odd and not greater than 10")
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.") 

if number > 10:
    print("The number is greater than 10.")
else:
    print("The number is not greater than 10.")



# cinema charges:
 # - Under 12 years: 200 PKR
  #- 12 to 17 years: 350 PKR  
   # 18 and above:   500 PKR
  #- 60 and above:   250 PKR (senior discount)
 # Set age = any number and print the ticket price.

age = 60      
if age < 12:
    print("Ticket price: 200 PKR")  
elif 12 <= age < 18:
    print("Ticket price: 350 PKR")  
elif 18 <= age < 60:
    print("Ticket price: 500 PKR")
else:
    print("Ticket price: 250 PKR (senior discount)")    