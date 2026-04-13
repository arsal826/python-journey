# Take this string:
# "the-quick-brown-fox-jumps-over-the-lazy-dog"

# → Split by dash
# → Count how many times each word appears
# → Print words that appear more than once
# → Join back with spaces in title case

sentence = "the-quick-brown-fox-jumps-over-the-lazy-dog"
# split the sentence into words
words = sentence.split("-")
# create an empty dictionary to store the word counts
word_counts = {}
# iterate through the words and count their occurrences
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
# print words that appear more than once
print("Words that appear more than once:")
for word, count in word_counts.items():
    if count > 1:
        print(f"{word}: {count}")
# join back with spaces in title case
modified_sentence = " ".join(word.title() for word in words)
print("Modified sentence:", modified_sentence)
