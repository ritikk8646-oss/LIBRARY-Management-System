from utils import books
def add():
    book_name=input("Enter the book you want to add: ").strip().upper()
    books[book_name]='Book Available'
    print(f"Book Added: {book_name}")