name = "arsal ahmad khan"

# your approach but for ANY length name
words = name.split()
result = []

for word in words:
    result.append(word.capitalize())

print(" ".join(result))

# Count how many vowels are in 'I am learning backend development'

sentence = "I am learning backend development"
vowels = "aeiouAEIOU"
count = 0
for char in sentence:
    if char in vowels:
        count += 1
        print(f"Found vowel: {char}")
print(f"Total vowels found: {count}")   

# Check if 'racecar' is a palindrome using slicing
word= "racecar"
if word == word[::-1]:
    print(f"{word} is a palindrome")
else:    
    print(f"{word} is not a palindrome")


#Take a sentence — print every word on a separate line  

sentence = "I am learning backend development"
words = sentence.split()
for word in words:
    print(word)     


#Take a sentence — print the longest word   
sentence = "I am learning backend development"
words = sentence.split()
longest_word = ""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word
print(f"The longest word is: {longest_word}")

#Replace every space in a sentence with a dash -
sentence = "I am learning backend development"
modified_sentence = sentence.replace(" ", "-")
print(modified_sentence)

#Check if a string starts with a capital letter — print True or False
sentence = "I am learning backend development"
print(sentence.startswith("I"))