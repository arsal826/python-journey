#Create a dictionary of 5 countries and their capitals. Print each one.

#· Create a phone book — add 3 contacts, search by name, delete one
# Given a list of students with grades, find who has the highest grade using a dict



countries = {
    'USA': 'Washington D.C.',
    'Canada': 'Ottawa',
    'UK': 'London',
    'France': 'Paris',
    'Japan': 'Tokyo'
}
for country, capital in countries.items():
    print(f"The capital of {country} is {capital}.")
#· Count how many times each word appears in 'the cat sat on the mat the cat'

sentence = 'the cat sat on the mat the cat'
word_count = {} 
for word in sentence.split():
    word_count[word] = word_count.get(word, 0) + 1

for word, count in word_count.items():
    print(f"'{word}': {count}")