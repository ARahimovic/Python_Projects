# Exercise 9: Complex Data Structures
# Task: Create a program that:
# 1. Creates a dictionary of dictionaries to represent a simplified library system
# 2. Each book should have a title, author, publication year, and status (available/borrowed)
# 3. Implement functions to:
#    a. Add a new book to the library
#    b. Display all books by a specific author
#    c. Check if a book is available
#    d. Borrow or return a book
#    e. Display all books published after a specific year


class Library:
     
    def __init__(self):
        # Main dictionary where books will be stored
        # We'll use book titles as keys and dictionaries of book attributes as values
        self.books = {}

    def add_book(self, title, author, year, status="available"):
        if not title or not author :
            return False, "Title and author cannot be empty"
        
        try:
            year = int(year)
        except ValueError:
            return False, "year must be integer"
    
        if title in self.books:
            return False, f"{title} alrady exist in library"

        self.books[title]= {
            'title':title,
            'author':author.lower(),
            'year':year,
            'status':status.lower()
        }

        return True, f"'{title}' added successfully"
    
    def isBookAvailable(self, title):
        if not title :
            return False, "title name should be a non-empty string"

        if not title in self.books:
            return False, f"'{title}' is not found in the library"
        
        if self.books[title]['status'] =='available':
            return True
        else:
            return False, f"'{title}' is currently borrowed"
            

    def BorrowBook(self, title):
        if not title in self.books:
            return False, f"'{title}' is not found in the library"
        
        if self.books[title]['status'] == 'borrowed':
            return False, f"{title} is already borrowed"
        
        #Available, so we borrow it
        self.books[title]['status'] = 'borrowed'
        return True, f"'{title}' has been borrowed succefully"
        
    def returnBook(self, title):
        if not title in self.books:
            return False, f"'{title}' is not found in the library"

        if self.books[title]['status'] == 'available':
            return False, f"{title} is available"
        
        #it is borrowed, so we can return it
        self.books[title]['status'] = 'available'
        return True, f"'{title}' has been returned succefully"
        
    def displayAuthorBooks(self, authorName):
        authorBooks = [book for book in self.books.values() if book.get('author') == authorName.lower()]
        return authorBooks
        
    def allBooksAfterYear(self, year):
        try :
            year = int(year)
        except ValueError:
            return [], f"'{year}' year must be an integer"
        
        filtered_books = [book for book in self.books.values() if book.get('year') > year]
        return filtered_books
       

def main():
    library = Library()
    
    # Add some books
    library.add_book("To Kill a Mockingbird", "Harper Lee", 1960)
    library.add_book("1984", "George Orwell", 1949)
    library.add_book("Animal Farm", "George Orwell", 1945)
    
    # Test book availability
    print(library.isBookAvailable("1984"))
    
    # Borrow a book
    print(library.BorrowBook("1984"))
    
    # Check availability after borrowing
    print(library.isBookAvailable("1984"))
    
    # Display books by author
    print("Books by George Orwell:")
    for book in library.displayAuthorBooks("George Orwell"):
        print(f"- {book['title']} ({book['year']})")
    
    # Display books after a year
    print("Books after 1950:")
    for book in library.allBooksAfterYear(1950):
        print(f"- {book['title']} by {book['author']} ({book['year']})")

if __name__ == "__main__":
    main()