sentence = "the quick brown fox jumps over the lazy dog"
# → Print every word longer than 3 letters
# → Print the longest word
# → Count how many words start with a vowel
vowel_count = 0
vowels = "aeiou"
sentence = sentence.split()
longest_word = ""
for word in sentence:
    if len(word) > 3:
        print(word)
    if len(word) > len(longest_word):
        longest_word = word
print("Longest word:", longest_word)
for word in sentence:
    if word[0].lower() in vowels:
        vowel_count += 1
print("Number of words starting with a vowel:", vowel_count)