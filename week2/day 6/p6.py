# A function that takes a list of dicts
# each dict has "name" and "salary"
# return the name of highest paid person

def highest_paid(people):
    if not people:
        return None  # Return None if the list is empty

    highest_paid_person = people[0]  # Start with the first person as the highest paid

    for person in people[1:]:  # Iterate through the rest of the people
        if person["salary"] > highest_paid_person["salary"]:
            highest_paid_person = person  # Update if we find a higher salary

    return highest_paid_person["name"]  # Return the name of the highest paid person

# Example usage
people = [
    {"name": "Alice", "salary": 70000},
    {"name": "Bob", "salary": 85000},
    {"name": "Charlie", "salary": 60000}
]
result = highest_paid(people)
print("The highest paid person is:", result)