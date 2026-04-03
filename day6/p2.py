# Take this string:
# "python-is-the-best-language-for-backend"
# Split by dash
# Print each word on separate line
# Then join them back with spaces
# Print the final result in uppercase

sentence = "python-is-the-best-language-for-backend"
for word in sentence.split("-"):
    print(word)
print(" ".join(sentence.split("-")).upper())


# Write a function called second_largest(lst)
# It finds and returns the second largest 
# number in a list WITHOUT using sort()

# numbers = [10, 25, 3, 47, 8, 33, 15, 62, 7]
# second_largest(numbers) → 47

numbers = [10, 25, 3, 47, 8, 33, 15, 62, 7]
def second_largest(lst):
    max_number = lst[0]
    second_largest = lst[0]
    for number in lst:
        if number > max_number:
            second_largest = max_number
            max_number = number
        elif number > second_largest and number != max_number:
            second_largest = number
    return second_largest

print(second_largest(numbers))


# You have:
# products = [
#     {"name": "laptop",  "price": 150000, "stock": 5},
#     {"name": "phone",   "price": 80000,  "stock": 0},
#     {"name": "tablet",  "price": 60000,  "stock": 3},
#     {"name": "watch",   "price": 25000,  "stock": 0},
#     {"name": "earbuds", "price": 15000,  "stock": 8}
# ]

# Print only items that are IN stock
# Print the most expensive item
# Print the total value of all stock
# (price × stock for each, then total)
products = [
    {"name": "laptop",  "price": 150000, "stock": 5},
    {"name": "phone",   "price": 80000,  "stock": 0},
    {"name": "tablet",  "price": 60000,  "stock": 3},
    {"name": "watch",   "price": 25000,  "stock": 0},
    {"name": "earbuds", "price": 15000,  "stock": 8}
]
for name, price, stock in products:
    if stock > 0:
        print(f"{name} is in stock")
most_expensive = products[0]
total_value = 0
for product in products:
    if product["price"] > most_expensive["price"]:
        most_expensive = product
    total_value += product["price"] * product["stock"]
print(f"The most expensive item is {most_expensive['name']}")
print(f"The total value of all stock is {total_value}")


# Take this paragraph:
# "I love Python. Python is great. 
# I use Python for backend. 
# Backend development is my goal."

# Count every word (ignore punctuation, 
# ignore capital vs lowercase)
# Print top 3 most repeated words

paragraph = "I love Python. Python is great. I use Python for backend. Backend development is my goal."
word_count = {}
for word in paragraph.split():
    word = word.strip(".").lower()
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Sort the words by count in descending order and print the top 3
for word, count in sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:3]:
    print(f"{word}: {count}")

# Write a function called analyze_text(text)
# It takes any string and returns a dictionary
# with these keys:

# {
#   "total_words": ?,
#   "unique_words": ?,
#   "longest_word": ?,
#   "shortest_word": ?,
#   "most_common_word": ?,
#   "average_word_length": ?
# }

# Test it with:
# "I am learning Python and Python is 
# the best language for backend development"

# Print each key and value clearly

def analyze_text(text):
    words = text.split()
    total_words = len(words)
    unique_words = set(words)
    longest_word = max(words, key=len)
    shortest_word = min(words, key=len)
    most_common_word = max(set(words), key=words.count)
    average_word_length = sum(len(word) for word in words) / total_words

    return {
        "total_words": total_words,
        "unique_words": len(unique_words),
        "longest_word": longest_word,
        "shortest_word": shortest_word,
        "most_common_word": most_common_word,
        "average_word_length": average_word_length
    }

# Test the function
text = "I am learning Python and Python is the best language for backend development"
analysis = analyze_text(text)
for key, value in analysis.items():
    print(f"{key}: {value}")