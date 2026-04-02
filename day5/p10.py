def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c

while True:
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        c = int(input("Enter third number: "))
        if a < 0 or b < 0 or c < 0:
            print("Please enter non-negative integers only.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter integers only.")

result = greatest(a,b,c)
print("The greatest number is:", result)
