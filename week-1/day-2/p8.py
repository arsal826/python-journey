#Create a list of 5 cities. Print each one using a for loop.
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
for city in cities:
    print(city)     


    #· Create a list of numbers. Print only the ones greater than 50.
numbers = [10, 25, 50, 75, 100]
counter = 0 
for number in numbers:
    if number > 50:
        print(number)
        counter += 1
print(f"There are {counter} numbers greater than 50.")           