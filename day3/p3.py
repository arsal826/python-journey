def is_valid_age(age):
    return 0 <= age <= 120

while True:
    age = int(input("Enter your age: "))
    if is_valid_age(age):
        print(f"Your age {age} is valid.")
        break
    else:
        print("Invalid age. Please enter a number between 0 and 120.")