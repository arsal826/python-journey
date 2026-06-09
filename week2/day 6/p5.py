# Write a function called compare_students(s1, s2)
# It takes two student dictionaries like:
# {"name": "Ali", "grade": 85, "age": 20}

# It prints:
# → Who has higher grade
# → Who is older
# → If grades are equal print "Tie"
# → Return the student with higher grade

# compare_students(
#     {"name": "Ali",  "grade": 85, "age": 20},
#     {"name": "Sara", "grade": 92, "age": 19}
# )

# Output:
# Sara has higher grade (92 vs 85)
# Ali is older (20 vs 19)
# Returns: Sara's dict
def compare_students(s1, s2):
    if s1["grade"] > s2["grade"]:
        print(f"{s1['name']} has higher grade ({s1['grade']} vs {s2['grade']})")
        higher_grade_student = s1
    elif s2["grade"] > s1["grade"]:
        print(f"{s2['name']} has higher grade ({s2['grade']} vs {s1['grade']})")
        higher_grade_student = s2
    else:
        print("Tie")
        higher_grade_student = None

    if s1["age"] > s2["age"]:
        print(f"{s1['name']} is older ({s1['age']} vs {s2['age']})")
    elif s2["age"] > s1["age"]:
        print(f"{s2['name']} is older ({s2['age']} vs {s1['age']})")
    else:
        print("Both students are the same age")

    return higher_grade_student

# Example usage
result = compare_students(
    {"name": "Ali",  "grade": 85, "age": 19},
    {"name": "Sara", "grade": 92, "age": 19}
)
print("Returns:", result)
