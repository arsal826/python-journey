text = "the quick brown fox the lazy dog the end"

# Count how many times each word appears
# Print the most repeated word
# Print all words that appear only once

# Split the text into words
words = text.split()
counts = {}
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

# Print the most repeated word
most_repeated = max(counts, key=counts.get)
print(f"Most repeated word: {most_repeated}")

# Print all words that appear only once
once_words = [word for word, count in counts.items() if count == 1]
print(f"Words that appear only once: {once_words}")