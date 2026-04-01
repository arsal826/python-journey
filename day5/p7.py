# Create a dictionary from two lists:
#     keys =   ["name", "age", "city"]
#     values = ["Arsal", 23, "Lahore"]
#     Expected: {"name":"Arsal","age":23,"city":"Lahore"}
#     Hint: use zip()
keys =   ["name", "age", "city"]
values = ["Arsal", 23, "Lahore"]
my_dict = dict(zip(keys, values))
print(my_dict)

# Count how many students got each grade:
#     grades = [85, 92, 67, 85, 78, 92, 85, 67]
#     Expected output:
#     85: 3 students
#     92: 2 students
#     67: 2 students
#     78: 1 student
grades = [85, 92, 67, 85, 78, 92, 85, 67]
grade_count = {}
for grade in grades:
    if grade in grade_count:
        grade_count[grade] += 1
    else:
        grade_count[grade] = 1

for g, c in grade_count.items():
    print(f"{g}: {c} students")