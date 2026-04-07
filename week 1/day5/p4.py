# Reverse every word in this sentence but 
#    keep the word order:
#    "Python is very powerful"
#     Expected: "nohtyP si yrev lufrewop"
sentence = "Python is very powerful"
words = sentence.split()
reversed_words = []
for word in words:
    reversed_words.append(word[::-1])   
print(" ".join(reversed_words))

# Count how many words in this sentence
#    are longer than 4 letters:
#    "I am learning backend development with Python"    
sentence = "I am learning backend development with Python"
words = sentence.split()
count = 0
for word in words:
    if len(word) > 4:
        count += 1  
print("Number of words longer than 4 letters:", count)

# Take this string: "hello-world-python-backend"
#    Replace dashes with spaces
#    Then print it in title case
#    Expected: "Hello World Python Backend"
sentence = "hello-world-python-backend"
sentence = sentence.replace("-", " ")
print(sentence.title())

# Check if two strings are anagrams
#    (same letters, different order)
#    word1 = "listen"
#    word2 = "silent"
#    Hint: sort both strings and compare
word1 = "listen"
word2 = "silent"
if sorted(word1) == sorted(word2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")

# Take a sentence from user using input()
#    Print how many times each vowel appears
#    a:? e:? i:? o:? u:?

sentence = input("Enter a sentence: ")
vowels = "aeiou"
count={"a":0, "e":0, "i":0, "o":0, "u":0}
for char in sentence:
    if char.lower() in vowels:
        count[char.lower()] += 1
for vowel, frequency in count.items():
    print(f"{vowel}: {frequency}")


