# lib/cli.py

from helpers import (
    exit_program,
    delete_book,
    list_books,
    find_book_by_id,
    create_book,
    find_book_by_name,
    create_author,
    delete_author,
    find_author_by_id,
    list_authors,
    find_author_by_name
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_books()
        elif choice == "2":
            list_authors()
        elif choice == "3":
            create_book()
        elif choice == "4":
            create_author()   
        elif choice == "5":
            delete_book()
        elif choice == "6":
            delete_author()
        elif choice == "7":
            find_book_by_id()
        elif choice == "8":
            find_author_by_id()
        elif choice == "9":
            find_book_by_name()
        elif choice == "10":
            find_author_by_name()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all books")
    print("2. List all authors")
    print("3. Create a book")
    print("4. Create an author")
    print("5. Delete a book")
    print("6. Delete an author")
    print("7. Find book by id")
    print("8. Find author by id")
    print("9. Find book by name")
    print("10. Find author by name")



if __name__ == "__main__":
    main()
