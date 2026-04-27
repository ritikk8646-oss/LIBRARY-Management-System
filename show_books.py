from utils import books
def show():
    
    if len(books)==0:
        print("Book not available")
    else:
        for book in books:
            print(book)