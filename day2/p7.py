# bmi calculator anmd telling ypu are over weight OR UNDER WEIGHT OR NORMAL
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))
bmi = weight / (height ** 2)

if bmi < 18.5:  
    print("You are underweight.")
elif 18.5 <= bmi < 25:  
    print("You are normal weight.") 
else:    print("You are overweight.")   

