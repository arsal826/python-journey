#Create a list of 5 numbers — print only the even ones
numbers=[1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        print(num)


names = ["Alice", "Bob", "Charlie", "David", "Eve"]
names.sort()

for name in names:
    print(name)

#reate a list of numbers — remove all numbers below 5
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in numbers:
    if num < 5:
         numbers.remove(num)
print(numbers)  

#Create a list of names — print how many have more than 4 letters
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
count = 0
for name in names:
    if len(name) > 4:
        count += 1
print(f"Number of names with more than 4 letters: {count}")


#reate a list of prices — apply 10% discount to each and print new prices
prices = [100, 200, 300, 400, 500]
discounted_prices = []
for price in prices:
    discounted_price = price * 0.9
    discounted_prices.append(discounted_price)
print(f"Discounted prices: {discounted_prices}")


#Combine two lists into one and remove duplicates
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
result=[]
for item in list1+list2:
    if item not in result:
        result.append(item) 
print(f"Combined list without duplicates: {result}")