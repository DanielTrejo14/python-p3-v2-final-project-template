# lib/helpers.py
from models.book import Book
from models.author import Author

def helper_1():
    print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
    exit()



def find_book_by_id():
    id_ = input("Enter the book's ID: ")
    book = Book.find_by_id(id_)
    print(book) if book else print(f'Book {id_} not found')


def find_book_by_name():
    name = input("Enter the book's name: ")
    book = Book.find_by_name(name)
    print(book) if book else print(f'Book {name} not found')



def delete_book():
    book_id = input("Enter book's ID: ")
    name = Book.find_by_id(book_id)
    if book := Book.find_by_id(book_id):
        book.delete()
        print(f'{name.name} was deleted')
    else:
        print("Not found")

    
def list_books():
    books = Book.all_books()
    for book in books:
        print(book)


def create_book():
    name = input("Enter the book's name: ")
    date = input("Enter the book's date: ")
    author_id = input("Enter the author's ID: ")
    author = Author.find_by_id(author_id)
    if len(name) >= 2:
        if len(date) == 10:
            if author:
                if book := Book.create(name, date, author_id):
                    print(f'Success {book}')
                else:
                    print("Error creating book")
            else:
                print("Author not found")
        else:
            print("Date format has to be 00/00/0000")
    else:
        print("Name must be longer than 1 characters")



def create_author():
    name = input("Enter the author's name: ")
    if len(name) >= 2:
        if author := Author.create(name):
            print(f'Success {author}')
        else:
            print("Error creating author")
    else:
        print("Name must be longer than 1 character")



def delete_author():
    author_id = input("Enter author's ID: ")
    name = Author.find_by_id(author_id)
    if author := Author.find_by_id(author_id):
        author.delete()
        print(f'{name.name} was deleted')
    else:
        print("Not found")


def find_author_by_id():
    id_ = input("Enter the author's ID: ")
    author = Author.find_by_id(id_)
    print(author) if author else print(f'Author {id_} not found')



def list_authors():
    authors = Author.all_authors()
    for author in authors:
        print(author)


def find_author_by_name():
    name = input("Enter the author's name: ")
    author = Author.find_by_name(name)
    print(author) if author else print(f'Author {name} not found')