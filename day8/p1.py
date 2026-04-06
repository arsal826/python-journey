# Take this string:
# "my name is arsal and i am a backend developer"
# Print every word that:
# → starts with a vowel
# → AND is longer than 3 letters

sentence = "my name is arsal and i am a backend developer"
# split the sentence into words
words = sentence.split()  # ["my", "name", "is", "arsal", "and", "i", "am", "a", "backend", "developer"]

# define vowels
vowels = "aeiou"

# iterate through words
for word in words:
    # check if word starts with a vowel and is longer than 3 letters
    if word[0].lower() in vowels and len(word) > 3:
        print(word)
# You have:
# numbers = [5, 12, 8, 23, 4, 16, 7, 19, 3, 11]

# Without using any built in functions:
# → Print numbers that are prime
# → A prime number is only divisible by 1 and itself
# → 2, 3, 5, 7, 11, 13... are prime

# Hint: for each number check if anything 
# divides it evenly between 2 and the number itself

numbers = [5, 12, 8, 23, 4, 16, 7, 19, 3, 11]
for num in numbers:
    if num < 2:
        continue  # skip numbers less than 2
    is_prime = True  # assume number is prime until proven otherwise
    for divisor in range(2, num):
        if num % divisor == 0:
            is_prime = False  # found a divisor, not prime
            break
    if is_prime:
        print(num)
