# nvert a dictionary
#     swap keys and values
#     original = {"a": 1, "b": 2, "c": 3}
#     Expected: {1: "a", 2: "b", 3: "c"}




original = {"a": 1, "b": 2, "c": 3}
inverted = {}
for key, value in original.items():
    inverted[value] = key
print(inverted)