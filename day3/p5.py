#  write bmi(weight, height) — returns the BMI value
def bmi(weight, height):
    return weight / (height ** 2)

def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Value must be greater than 0.")
        except ValueError:
            print("Please enter a valid number.")

weight = get_positive_float("Enter your weight in kg: ")
height = get_positive_float("Enter your height in meters: ")

print("Valid inputs:", weight, height)

#rite bmi_category(bmi) — takes a BMI number, returns the category string
def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

#all bmi() then pass the result to bmi_category() and print the final result
bmi_value = bmi(weight, height)
category = bmi_category(bmi_value)
print(f"Your BMI is: {bmi_value:.2f} and you are categorized as: {category}")