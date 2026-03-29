import random

options = ["rock", "paper", "scissors"]

while True:
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower().strip()
    
    if user_choice not in options:
        print("Invalid input. Please enter rock, paper, or scissors.")
        continue
    
    computer_choice = random.choice(options)
    print(f"Computer chose: {computer_choice}")
    
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print(f"You win! {user_choice} beats {computer_choice}.")
    else:
        print(f"You lose! {computer_choice} beats {user_choice}.")
    
    play_again = input("Play again? (yes/no): ").lower().strip()
    if play_again != "yes":
        print("Thanks for playing!")
        break
