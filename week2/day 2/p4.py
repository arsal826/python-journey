sentence = "the cat sat on the mat and the cat sat again"
# split the sentence into words
words = sentence.split()
# create an empty dictionary to store the word counts
word_counts = {}
# iterate through the words and count their occurrences
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

# print the word counts
for word, count in word_counts.items():
    print(f"{word}: {count}")

# replace words with counts
for word in words:
    if word in word_counts:
        words[words.index(word)] = f"*** {word} ***"

# print the modified sentence
print(" ".join(words))