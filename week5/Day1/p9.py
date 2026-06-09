words = ["apple", "banana", "apple", "orange", "banana", "apple"]
frequency = {}
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1
print("Word frequencies:")
for word, count in frequency.items():
    print(f"{word}: {count}")
    