# books = [
#     {"title": "Python Basics",    "genre": "tech",    "pages": 320, "borrowed": True},
#     {"title": "Clean Code",       "genre": "tech",    "pages": 464, "borrowed": False},
#     {"title": "Atomic Habits",    "genre": "self-help","pages": 320, "borrowed": True},
#     {"title": "Deep Work",        "genre": "self-help","pages": 296, "borrowed": False},
#     {"title": "FastAPI Guide",    "genre": "tech",    "pages": 280, "borrowed": True},
#     {"title": "Think Python",     "genre": "tech",    "pages": 300, "borrowed": False},
#     {"title": "Rich Dad Poor Dad","genre": "finance", "pages": 336, "borrowed": True}
# ]
# ```

# Calculate and print:
# ```
# → Total books per genre
# → Available books per genre (borrowed = False)
# → Average pages per genre
# → Longest book in each genre
# → How many books are currently borrowed
# → Total pages of all available books

books = [
    {"title": "Python Basics",    "genre": "tech",    "pages": 320, "borrowed": True},
    {"title": "Clean Code",       "genre": "tech",    "pages": 464, "borrowed": False},
    {"title": "Atomic Habits",    "genre": "self-help","pages": 320, "borrowed": True},
    {"title": "Deep Work",        "genre": "self-help","pages": 296, "borrowed": False},
    {"title": "FastAPI Guide",    "genre": "tech",    "pages": 280, "borrowed": True},
    {"title": "Think Python",     "genre": "tech",    "pages": 300, "borrowed": False},
    {"title": "Rich Dad Poor Dad","genre": "finance", "pages": 336, "borrowed": True}
]  
total_books = {}
available_books = {}
total_pages = {}
longest_book = {}
borrowed_count = 0
available_pages = 0

for book in books:
    genre = book["genre"]
    pages = book["pages"]
    borrowed = book["borrowed"]

    # Total books per genre
    if genre in total_books:
        total_books[genre] += 1
    else:
        total_books[genre] = 1

    # Available books per genre
    if not borrowed:
        if genre in available_books:
            available_books[genre] += 1
        else:
            available_books[genre] = 1

    # Average pages per genre
    if genre in total_pages:
        total_pages[genre] += pages
    else:
        total_pages[genre] = pages

    # Longest book in each genre
    if genre in longest_book:
        if pages > longest_book[genre]["pages"]:
            longest_book[genre] = {"title": book["title"], "pages": pages}
    else:
        longest_book[genre] = {"title": book["title"], "pages": pages}

    # Count borrowed books and total pages of available books
    if borrowed:
        borrowed_count += 1
    else:
        available_pages += pages

# Calculate average pages per genre
for genre in total_pages:
    total_pages[genre] /= total_books[genre]

# Print the results
for genre in total_books:
    print(f"Genre: {genre}")
    print(f"  Total books: {total_books[genre]}")
    print(f"  Available books: {available_books.get(genre, 0)}")
    print(f"  Average pages: {total_pages[genre]:.2f}")
    print(f"  Longest book: {longest_book[genre]['title']} ({longest_book[genre]['pages']} pages)")
    print()

print(f"Total borrowed books: {borrowed_count}")
print(f"Total pages of available books: {available_pages}")