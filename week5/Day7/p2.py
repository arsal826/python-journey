name = "arsal ahmad"
# Print in title case
# Print reversed
# Print number of vowels

print(name.title())
print(name[::-1])
vowels = "aeiou"
vowel_count = 0
for char in name:
    if char.lower() in vowels:
        vowel_count += 1
print(f"Number of vowels: {vowel_count}")