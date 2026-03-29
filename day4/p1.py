def add_student():
    while True:
        try:
            name=str(input("Enter student name: "))
            age=int(input("Enter student age: "))
            grade=float(input("Enter student grade: "))
            student={"name":name,"age":age,"grade":grade}
            students.append(student)
            print(f"{name} added successfully")
            break
        except ValueError:
            print("Please enter valid values for age and grade.")

students=[]
add_student()

