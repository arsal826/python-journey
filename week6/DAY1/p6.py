# Find the longest word in a sentence and its length

sentence = "I am learning backend development with python"

# Return the longest word and how many letters it has
# Expected output: development has 11 letters
# If there's a tie, pick the first one
words = sentence.split()
longest_word = ""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word
print(f"{longest_word} has {len(longest_word)} letters")
