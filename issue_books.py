from utils import books


 
def issue():
        book_name=input("Enter the book you want to issue: ").strip().upper()
        if book_name in books and books[book_name]:
            name=input("Enter the name: ")
            duration=int(input("Enter number of days: "))
            books[book_name]="Issued successfully"
            print(f"Book issued to {name} for {duration}")
        else:
            print("Book not available")
    
            
        
                
            
            
     