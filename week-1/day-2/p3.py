# Print a countdown from 10 to 1 using a while loop, then print 'Go!

countdown = 10
while countdown > 0:
    print(countdown)
    countdown = countdown - 1   

print("Go!")    

#Use a counter to count how many letters are in 'I am learning Python' (without using len())

sentence = "I am learning Python"
counter = 0 
for letter in sentence: 
    counter = counter + 1  

print("The number of letters in the sentence is:", counter)