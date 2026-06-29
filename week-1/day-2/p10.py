import random 
secter = random.randint(1, 10)
counter = 0
while True:
    guess = int(input("Guess a number between 1 and 10: "))
    counter += 1
    if guess < secter:
        print("Too low! Try again.")
    elif guess > secter:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number in {counter} tries.")
        break
    if counter >= 5:
        if secter % 2 == 0:
            print("Hint: The number is even.")
        else:
                print("Hint: The number is odd.")   