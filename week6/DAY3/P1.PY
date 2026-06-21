def add_book(book_id, title, author):
    try:
        try:
            with open("books.txt", "r") as file:
                for book in file:
                    b_id = book.strip().split(",")[0]
                    if b_id == book_id:
                        print("Book ID already exists.")
                        return
        except FileNotFoundError:
            pass

        with open("books.txt", "a") as file:
            file.write(
                f"{book_id},{title},{author},available,None,None\n"
            )

        print(f"Book '{title}' added successfully.")

    except Exception as e:
        print(f"Error: {e}")


def view_books():
    try:
        with open("books.txt", "r") as file:
            books = file.readlines()

        if not books:
            print("No books available.")
            return

        print("\nAll Books:")
        for book in books:
            book_id, title, author, status, borrower, borrow_date = (
                book.strip().split(",")
            )

            print(
                f"ID: {book_id}, Title: {title}, Author: {author}, "
                f"Status: {status}, Borrower: {borrower}, Borrow Date: {borrow_date}"
            )

    except FileNotFoundError:
        print("No books found.")


def borrow_book(book_id, borrower_name, borrow_date):
    try:
        with open("books.txt", "r") as file:
            books = file.readlines()

    except FileNotFoundError:
        print("No books found.")
        return

    found = False

    with open("books.txt", "w") as file:
        for book in books:
            b_id, title, author, status, borrower, old_date = (
                book.strip().split(",")
            )

            if b_id == book_id:
                found = True

                if status == "available":
                    file.write(
                        f"{b_id},{title},{author},borrowed,"
                        f"{borrower_name},{borrow_date}\n"
                    )

                    print(
                        f"Book '{title}' borrowed successfully by "
                        f"{borrower_name}."
                    )

                else:
                    file.write(book)
                    print("Book is already borrowed.")

            else:
                file.write(book)

    if not found:
        print("Book ID not found.")


def return_book(book_id):
    try:
        with open("books.txt", "r") as file:
            books = file.readlines()

    except FileNotFoundError:
        print("No books found.")
        return

    found = False

    with open("books.txt", "w") as file:
        for book in books:
            b_id, title, author, status, borrower, borrow_date = (
                book.strip().split(",")
            )

            if b_id == book_id:
                found = True

                if status == "borrowed":
                    file.write(
                        f"{b_id},{title},{author},available,None,None\n"
                    )

                    print(f"Book '{title}' returned successfully.")

                else:
                    file.write(book)
                    print("Book is already available.")

            else:
                file.write(book)

    if not found:
        print("Book ID not found.")


def available_books():
    try:
        with open("books.txt", "r") as file:
            books = file.readlines()

    except FileNotFoundError:
        print("No books found.")
        return

    available = False

    print("\nAvailable Books:")

    for book in books:
        book_id, title, author, status, borrower, borrow_date = (
            book.strip().split(",")
        )

        if status == "available":
            available = True
            print(f"ID: {book_id}, Title: {title}, Author: {author}")

    if not available:
        print("No available books.")

def menu():
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. View Available Books")
        print("6. Exit")
        try:
            choice = input("Enter your choice: ")
        except EOFError:
            print("\nInput error. Exiting the system.")
            break
        if choice == "1":
            book_id = input("Enter Book ID: ")
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            add_book(book_id, title, author)

        elif choice == "2":
            view_books()

        elif choice == "3":
            book_id = input("Enter Book ID to borrow: ")
            borrower_name = input("Enter Borrower's Name: ")
            borrow_date = input("Enter Borrow Date (YYYY-MM-DD): ")
            borrow_book(book_id, borrower_name, borrow_date)

        elif choice == "4":
            book_id = input("Enter Book ID to return: ")
            return_book(book_id)

        elif choice == "5":
            available_books()

        elif choice == "6":
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")