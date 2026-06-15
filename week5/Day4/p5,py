def add_student():
    name = input("Enter student name: ")
    if name == "":
        print("Name cannot be empty")
        return
    
    subject = input("Enter student subject: ")
    if subject == "":
        print("Subject cannot be empty")
        return
    
    try:
        score = int(input("Enter student score: "))
        if score < 0 or score > 100:
            print("Score must be between 0 and 100")
            return
    except ValueError:
        print("Score must be a number")
        return
    
    with open("students.txt", "a") as f:
        f.write(f"{name},{subject},{score}\n")
    print("Student added!")


def view_students():
    try:
        with open("students.txt", "r") as f:
            for line in f:
                parts = line.strip().split(",")
                print(f"{parts[0]} - {parts[1]}: {parts[2]}")
    except FileNotFoundError:
        print("No students yet. Add some first.")


def student_report(name):
    best_score = 0
    best_subject = ""
    total = 0
    count = 0
    found = False
    
    try:
        with open("students.txt", "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if parts[0] == name:
                    found = True
                    subject = parts[1]
                    score = int(parts[2])
                    print(f"{subject}: {score}")
                    total += score
                    count += 1
                    if score > best_score:
                        best_score = score
                        best_subject = subject
    except FileNotFoundError:
        print("No students yet. Add some first.")
        return
    
    if not found:
        print(f"No records found for {name}")
        return
    
    average = total / count
    print(f"\nReport for {name}:")
    print(f"Average: {average:.2f}")
    print(f"Best subject: {best_subject} ({best_score})")


def class_topper():
    students = {}
    
    try:
        with open("students.txt", "r") as f:
            for line in f:
                parts = line.strip().split(",")
                name = parts[0]
                score = int(parts[2])
                if name in students:
                    students[name].append(score)
                else:
                    students[name] = [score]
    except FileNotFoundError:
        print("No students yet. Add some first.")
        return
    
    topper = None
    highest_avg = 0
    for name, scores in students.items():
        avg_score = sum(scores) / len(scores)
        if avg_score > highest_avg:
            highest_avg = avg_score
            topper = name
    
    print(f"Class topper: {topper} with average {highest_avg:.2f}")


while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Student Report")
    print("4. Class Topper")
    print("5. Exit")
    
    choice = input("Choose an option (1-5): ")
    
    if choice not in ["1", "2", "3", "4", "5"]:
        print("Please enter a number between 1 and 5")
        continue
    
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        name = input("Enter student name: ")
        student_report(name)
    elif choice == "4":
        class_topper()
    elif choice == "5":
        print("Goodbye!")
        break