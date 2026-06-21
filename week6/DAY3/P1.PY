def add_book(book_id, title, author):
    try:
        with open("books.txt", "a") as file:
            file.write(f"{book_id},{title},{author},available\n")
        print(f"Book '{title}' added successfully.")
    except Exception as e:
        print(f"Error adding book: {e}")

def view_books():
    try:
        with open("books.txt", "r") as file:
            books = file.readlines()
        print("All Books:")
        for book in books:
            book_id, title, author, status = book.strip().split(",")
            print(f"ID: {book_id}, Title: {title}, Author: {author}, Status: {status}")
    except FileNotFoundError:
        print("No books found.")

def borrow_book(book_id):
    try:
        with open("books.txt", "r") as file:
            books = file.readlines()
    except FileNotFoundError:
        print("No books found.")
        return

    with open("books.txt", "w") as file:
        for book in books:
            b_id, title, author, status = book.strip().split(",")
            if b_id == book_id and status == "available":
                file.write(f"{b_id},{title},{author},borrowed\n")
                print(f"Book '{title}' borrowed successfully.")
            else:
                file.write(book)

def return_book(book_id):
    try:
        with open("books.txt", "r") as file:
            books = file.readlines()
    except FileNotFoundError:
        print("No books found.")
        return

    with open("books.txt", "w") as file:
        for book in books:
            b_id, title, author, status = book.strip().split(",")
            if b_id == book_id and status == "borrowed":
                file.write(f"{b_id},{title},{author},available\n")
                print(f"Book '{title}' returned successfully.")
            else:
                file.write(book)
def search_book(title):
    try:
        with open("books.txt", "r") as file:
            books = file.readlines()
    except FileNotFoundError:
        print("No books found.")
        return

    found = False
    for book in books:
        book_id, b_title, author, status = book.strip().split(",")
        if title.lower() in b_title.lower():
            print(f"ID: {book_id}, Title: {b_title}, Author: {author}, Status: {status}")
            found = True
    if not found:
        print(f"No books found with title containing '{title}'.")
def available_books():
    try:
        with open("books.txt", "r") as file:
            books = file.readlines()
    except FileNotFoundError:
        print("No books found.")
        return

    print("Available Books:")
    for book in books:
        book_id, title, author, status = book.strip().split(",")
        if status == "available":
            print(f"ID: {book_id}, Title: {title}, Author: {author}")
def menu():
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Search Book by Title")
        print("6. View Available Books")
        print("7. Exit")

        try:
            choice = input("Enter your choice: ")
        except KeyboardInterrupt:
            print("\nExiting the system.")
            break

        if choice == "1":
            book_id = input("Enter book ID: ")
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            add_book(book_id, title, author)
        elif choice == "2":
            view_books()
        elif choice == "3":
            book_id = input("Enter book ID to borrow: ")
            borrow_book(book_id)
        elif choice == "4":
            book_id = input("Enter book ID to return: ")
            return_book(book_id)
        elif choice == "5":
            title = input("Enter title to search: ")
            search_book(title)
        elif choice == "6":
            available_books()
        elif choice == "7":
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")
            
menu()