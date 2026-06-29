sentence="the cat sat on the mat and the cat sat again"
# split the sentence into words
words = sentence.split()
# create an empty dictionary to store the word counts
word_counts = {}
# iterate through the words and count their occurrences
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1
# print the word counts
for word, count in word_counts.items():
    print(f"{word}: {count}")