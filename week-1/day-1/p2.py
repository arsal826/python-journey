first = "Arsal"
last = "Ahmad"
full = first + " " + last
age = 22
print(full)
print(len(full))
print(full.upper())
print(full.lower())
print(f"My name is {full} and I am {age} years old")

# Store your name, city, and age in variables. 
# Print a sentence using all three.
# Expected: "My name is Arsal, I am from Lahore, I am 22 years old"
name = "Arsal"
city = "Lahore"
age = 22
print(f"my name is {name}, i am from {city}, i am {age} years old")


#Take any string and print:
 #  - its length
 #  - all uppercase
  # - all lowercase
   #- first letter only (hint: "hello"[0] gives "h")     

string = "Hello World"
print(len(string))
print(string.upper())   
print(string.lower())
print(string[0])    


name = "arsal ahmad"
print(name.capitalize())
print(name[0].upper() + name[1:11])


#Take a full name like "Arsal Khan" and print 
  # the first name and last name on separate lines
name = "Arsal ahmad"
print(name[0:5])
print(name[6:11 ])

name = "Muhammad Ali"

#1. Print just "Muhammad" using slicing
#2. Print just "Ali" using slicing
#3. Print the last letter using negative index
#4. Print the first 3 letters
#5. Print the name backwards
 #  (hint: name[::-1] — try it and think about why it works)

parts = name.split()
print(parts[0])
print(parts[1])     
print(name[-1])         
print(name[0:3])
print(name[::-1])

name = "Arsal"

print(name[::2])   # what do you expect? run it and see
print(name[::1])   # what about this?
print(name[::-2])  # and this?  