#Create a dictionary for a person
#with name, age, city, is_student
#Add a new key called "grade"
#Update the age
#Delete the city
#Loop through and print every key and value

person = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "is_student": False
}
# Add a new key called "grade"
person["grade"] = 85.5

# Update the age
person["age"] = 31

# Delete the city
del person["city"]

# Loop through and print every key and value
for key, value in person.items():
    print(f"{key}: {value}")


    #Keep asking user for a password
#until they type "python123"
#Count how many attempts they made
#Print "Access granted in X attempts"


attempts = 0
while True:
    password = input("Enter the password: ").lower()
    attempts += 1
    if password == "python123":
        print(f"Access granted in {attempts} attempts")
        break
    else:
        print("Incorrect password. Try again.")