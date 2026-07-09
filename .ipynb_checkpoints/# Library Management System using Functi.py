# Library Management System using Functions (def)

books = []

def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    quantity = int(input("Enter Quantity: "))

    book = {
        "ID": book_id,
        "Title": title,
        "Author": author,
        "Quantity": quantity
    }

    books.append(book)
    print("Book added successfully!")

def view_books():
    if len(books) == 0:
        print("No books available.")
    else:
        print("\n----- Book List -----")
        for book in books:
            print("Book ID :", book["ID"])
            print("Title   :", book["Title"])
            print("Author  :", book["Author"])
            print("Quantity:", book["Quantity"])
            print("---------------------")

def search_book():
    title = input("Enter Book Title: ")

    for book in books:
        if book["Title"].lower() == title.lower():
            print("\nBook Found")
            print("Book ID :", book["ID"])
            print("Title   :", book["Title"])
            print("Author  :", book["Author"])
            print("Quantity:", book["Quantity"])
            return

    print("Book not found.")

def delete_book():
    book_id = input("Enter Book ID to delete: ")

    for book in books:
        if book["ID"] == book_id:
            books.remove(book)
            print("Book deleted successfully!")
            return

    print("Book not found.")

def menu():
    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Delete Book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            print("Thank you!")
            break
        else:
            print("Invalid choice.")

# Start the program
menu()