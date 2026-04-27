
from utils import books





        
def return_books():
    book_name = input("Enter book name: ").upper()

    if book_name in books:
        if books[book_name] == "Issued successfully":
            extra_days = int(input("Enter extra days: "))
            fine = 0

            if extra_days <= 7:
                fine = extra_days * 10
            elif extra_days <= 14:
                fine = (7 * 10) + (extra_days - 7) * 20
            else:
                fine = (7 * 10) + (7 * 20) + (extra_days - 14) * 60

            print("Fine:", fine)

            books[book_name] = "Book Available"
            print("Book returned")
        else:
            print("Book was not issued")
  
    else:
        print("Book is not from our library.")
        
  
        
     