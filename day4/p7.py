sentence = 'the cat sat on the mat the cat'
words = sentence.split()
print(words)

#reate a phone book — add 3 contacts, search by name, delete one
phone_book = {}
phone_book['alice'] = '123-456-7890'
phone_book['bob'] = '987-654-3210'
phone_book['charlie'] = '555-555-5555'

# Search by name
name_to_search =input("Enter a name to search: ").lower().strip()
if name_to_search in phone_book:
    print(f"{name_to_search}'s phone number is: {phone_book[name_to_search]}")
else:
    print(f"{name_to_search} not found in phone book.")
# Delete one contact
name_to_delete = input("Enter a name to delete: ").lower().strip()
if name_to_delete in phone_book:
    del phone_book[name_to_delete]
    print(f"{name_to_delete} has been deleted from the phone book.")
else:   
    print(f"{name_to_delete} not found in phone book.") 

