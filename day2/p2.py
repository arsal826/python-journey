number=1
count=0
while number <=50:
    if number % 3 ==0:
        count = count + 1
    number = number + 1
   
   
print("the numvers that are divisible by 3 between 1 and 50 are:", count)

# number = the number we are checking (1,2,3...50)
# count  = how many are divisible by 3

numbe = 1
counte = 0          # start at 0, not 1

while numbe <= 50:
    if numbe % 3 == 0:
        counte = counte + 1
    numbe = numbe + 1    # move to next number

print("Numbers divisible by 3 between 1 and 50:", counte)