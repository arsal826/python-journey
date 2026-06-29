with open("students.txt", "w") as file:
    file.write("Arsal,Math,85\n")
    file.write("Arsal,Science,90\n")
    file.write("Ahmed,Math,70\n")
    file.write("Ahmed,Science,80\n")
    file.write("Sara,Math,95\n")
    file.write("Sara,Science,88\n")
students = {}
with open("students.txt", "r") as file:
    for line in file:
        name, subject, score = line.strip().split(",")
        score = int(score)
        if name in students:
            students[name].append(score)
        else:
            students[name] = [score]
averages = {name: sum(scores) / len(scores) for name, scores in students.items()}
highest_avg_student = max(averages, key=averages.get)
print("Each student's average:")
for name, avg in averages.items():
    print(f"{name}: {avg:.2f}")
print(f"Student with the highest average: {highest_avg_student}")