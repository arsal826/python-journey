#You have a shop. An item costs 350 PKR.
 #  Someone buys 7 of them.
  # They pay with a 3000 PKR note.
   #Print the total cost and the change they receive.

cost = 350
quantity = 7
total_cost = cost * quantity
payment = 3000
change = payment - total_cost
print(f"Total cost: {total_cost} PKR and Yur Change is {change} PKR")


# student scored 67 out of 80 in a test.
 # Calculate and print their percentage.
  #Print whether they passed (passing is 50%).

score = 67
total_marks = 80
percentage = (score / total_marks) * 100
print(f"Percentage: {percentage:.2f}%")

if percentage >= 50:
    print("The student has passed.")
else:
    print("The student has failed.")



   #Print the area AND perimeter of a rectangle.
  #Width = 12, Height = 8
  #Area formula: width × height
   #erimeter formula: 2 × (width + height)

width = 12
height = 8
area = width * height
perimeter = 2 * (width + height)            

print(f"Area: {area} square units and Perimeter: {perimeter} units")    