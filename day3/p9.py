def add_student():
    name = input("Enter student name: ").strip()
    age = input("Enter student age: ").strip()
    grade = input("Enter student grade: ").strip()
    student = {"name": name, "age": age, "grade": grade}
    students.append(student)
    print(f"{name} added successfully")
def view_all():
   for student in students:
       print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
def find_student():
    name = input("Enter student name to find: ").strip()
    for student in students:
        if student['name'].lower() == name.lower():
            print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
            return
    print("Student not found.")
def class_average():
    if len(students) == 0:
        print("No students yet.")
        return
    total = 0
    for student in students:
        grade = float(student['grade'])
        total = total + grade
    average = total / len(students)
    print(f"Class average: {average:.2f}")
def highest_grade():
    if len(students) == 0:
        print("No students yet.")
        return
    highest = max(float(student['grade']) for student in students)
    print(f"Highest grade: {highest:.2f}")
def lowest_grade():
    if len(students) == 0:
        print("No students yet.")
        return
    lowest = min(float(student['grade']) for student in students)
    print(f"Lowest grade: {lowest:.2f}")
def delete_student():
    name = input("Enter student name to delete: ").strip()
    for i, student in enumerate(students):
        if student['name'].lower() == name.lower():
            del students[i]
            print("Student deleted.")
            return
    print("Student not found.")

students = []

while True:
    print("\n================================")
    print("     Student Grade Manager")
    print("================================")
    print("1. Add student")
    print("2. View all students")
    print("3. Find a student")
    print("4. Class average")
    print("5. Highest scorer")
    print("6. Lowest scorer")
    print("7. Delete student")
    print("8. Exit")
    print("================================")
    
    choice = input("Choose (1-8): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_all()
    elif choice == "3":
        find_student()
    elif choice == "4":
        class_average()
    elif choice == "5":
        highest_grade()
    elif choice == "6":
        lowest_grade()
    elif choice == "7":
        delete_student()
    elif choice == "8":
        print("Goodbye")
        break
    else:
        print("Invalid choice. Pick 1-8")