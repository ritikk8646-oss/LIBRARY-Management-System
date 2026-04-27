from add_books import add
from show_books import show
from issue_books import issue
from return_books import return_books
 
     
def library():
    
        while True:
            print("\n1. Add Book")
            print("2. Show Book")
            print("3. Issue Book")
            print("4. Return Book")
            print("5. Exit\n")
            choice = int(input("Enter your choice: "))
        
            if choice==1: add()
            elif choice==2: show()
            elif choice==3: issue()
            elif choice==4: return_books() 
            elif choice==5: 
                print("Thank you")
                break
            else:
                print("Invalid choice")
           
library()