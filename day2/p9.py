#Create a list of names. Count how many names have more than 4 letters.     
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
short_names = []
count = 0
for name in names:
    if len(name) > 4:
        count += 1
        short_names.append(name)
print(f"There are {count} names with more than 4 letters.")
print(f"The names with more than 4 letters are: {short_names}")


#Create a list of numbers. Make a new list with only the even ones.
numbers = [10, 25, 50, 75, 100,50,60,70,80]
even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
print(f"The even numbers are: {even_numbers}")