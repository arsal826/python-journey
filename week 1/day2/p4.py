#Keep asking for a number using while loop — stop when user enters 0 (use input())

while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        print("Stopping the loop.")
        break
    else:
        print(f"You entered: {num}")    