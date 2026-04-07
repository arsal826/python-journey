# Take this sentence:
# "the cat sat on the mat and the cat sat again"

# → Find all words that appear more than once
# → Print them with their count
# → Print the sentence with duplicate 
#    words replaced by "***"
   
# Expected:
# "the" appears 3 times
# "cat" appears 2 times
# "sat" appears 2 times

# "*** cat *** on *** mat and *** *** sat again"

sentence = "the cat sat on the mat and the cat sat again"
# Step 1: Split the sentence into words
words = sentence.split()
# Step 2: Count the occurrences of each word
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
# Step 3: Find words that appear more than once and print their counts
duplicates = {}
for word, count in word_count.items():
    if count > 1:
        duplicates[word] = count

for word, count in duplicates.items():
    print(f'"{word}" appears {count} times')

# Step 4: Print the sentence with duplicate words replaced by "***"
new_sentence = " ".join(["***" if word in duplicates else word for word in words])
print(f'\n{new_sentence}')