#ake the string "i love python programming"
#rint it as "I Love Python Programming"
#ut do it using only:
# .split()
# .join()
# string indexing
# .upper()

sentence = "i love python programming"
words = sentence.split()
capitalized_words = [word[0].upper() + word[1:] for word in words]
result = " ".join(capitalized_words)
print(result)

#ake the sentence "I am learning Python"
#rint each word reversed but keep 
#he word order the same

for word in sentence.split():
    reversed_word = word[::-1]
    print(reversed_word, end=' ')