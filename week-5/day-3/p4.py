# Save these 5 names to a file called names.txt
# one name per line
names = ["Arsal", "Ahmed", "Sara", "Ali", "Zara"]
# write a loop that saves each name
with open("names.txt", "w") as f:
    for name in names:
        f.write(name + "\n")  # add a newline after each name
    # Read names.txt back
# print each name with a number
# Expected:
# 1. Arsal
# 2. Ahmed
# 3. Sara
with open("names.txt", "r") as f:
    for i in range(len(names)):
        name = f.readline().strip()  # read a line and remove \n
        print(f"{i+1}. {name}")
# Append 2 more names to names.txt
# without deleting the existing 5
# Then read and print all 7
new_names = ["Hassan", "Aisha"]
with open("names.txt", "a") as f:  # 'a' for append
    for name in new_names:
        f.write(name + "\n")

with open("names.txt", "r") as f:
    dataOffILE=f.read()
    dataOffILE=dataOffILE.lower()  # read the whole file
    if "arsal" in dataOffILE:
        print("Arsal is in the file")
        