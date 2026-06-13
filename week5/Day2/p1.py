sentence = "i am learning python backend development"
# → Title case without .title()
# → Count vowels
# → Print words longer than 5 letters
# Title case without .title()
title_case_sentence = ""
for word in sentence.split():
    title_case_sentence += word[0].upper() + word[1:] + " "
print(title_case_sentence.strip())
# Count vowels
vowel_count = 0
for char in sentence:
    if char in "aeiouAEIOU":
        vowel_count += 1 
print("Number of vowels:", vowel_count)
# Print words longer than 5 letters
for word in sentence.split():
    if len(word) > 5:
        print(word)