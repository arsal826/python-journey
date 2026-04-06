# Take this messy string:
# "  Hello,   my   name   is   Arsal.  
# I   am   learning   Python!!  
# This   is   amazing...  "

# Clean it up:
# → Remove extra spaces between words
# → Remove punctuation (. , ! ?)
# → Print it properly capitalized
# Expected: "Hello my name is Arsal I am 
# learning Python This is amazing"

sentence = "  Hello,   my   name   is   Arsal.  I   am   learning   Python!!  This   is   amazing...  "
cleaned = ""
for char in sentence:
    if char.isalnum() or char.isspace():
        cleaned += char
cleaned = cleaned.strip()
cleaned = cleaned.replace(".", "").replace(",", "").replace("!", "").replace("?", "")
print(cleaned.capitalize())

