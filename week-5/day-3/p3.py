with open("data.txt", "r") as f:
    lines = f.readlines()
    print(lines)

# loop through each line
with open("data.txt", "r") as f:
    for line in f:
        print(line.strip())  # strip removes the \n