# Write a function called palindrome_checker(words)
# Takes a list of words
# Prints which ones are palindromes

words = ["racecar", "hello", "level", "python", "madam"]
def palindrome_checker(words):
    for word in words:
        if word == word[::-1]:
            print(f"{word} is a palindrome.")
        else:
            print(f"{word} is not a palindrome.")
palindrome_checker(words)
