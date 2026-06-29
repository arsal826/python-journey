with open("data.txt", "w") as f:
    f.write("Hello Arsal\n")
    f.write("This is my first saved file\n")

print("Done writing")

with open("data.txt", "r") as f:
    data=f.read()
    print(data)
    
with open("data.txt", "a") as f:
    f.write("This line was added later\n")

# read again to see all 3 lines
with open("data.txt", "r") as f:
    print(f.read())