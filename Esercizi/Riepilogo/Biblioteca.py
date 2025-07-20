class Book:
    def __init__(self, book_id: str, title: str, author: str) -> None:
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        self.is_borrowed = True
        return self.is_borrowed

    def return_book(self):
        self.is_borrowed = False
        return self.is_borrowed

class Member:
    def __init__(self, member_id: str, name: str) -> None:
        self.member_id = member_id
        self.name = name
        self.borrowed_books: list[Book] = []

    def borrow_book(self, book: Book):
        if book not in self.borrowed_books:
            self.borrowed_books.append(book.title)
        else:
            raise ValueError("Member_borrow_book")
        
    def return_book(self, book: Book):
        if book.title in self.borrowed_books:
            self.borrowed_books.remove(book.title)
        else:
            raise ValueError("Member_return_book")

class Library:
    def __init__(self) -> None:
        self.books: dict[str, Book] = {}
        self.members: dict[str, Member] = {}
        
    def add_book(self, book_id: str, title: str, author: str):
        
        book = Book(book_id, title, author)
        if book_id not in self.books:
            self.books[book_id] = book
            return self.books
        else:
            raise ValueError("add_book")
        
    def register_member(self, member_id:str, name: str):

        self.member = Member(member_id, name)
        if member_id not in self.members:
            self.members[member_id] = self.member
            return self.members
        else:
            raise ValueError("register_member")
        
    def borrow_book(self, member_id: str, book_id: str):
        
        if member_id not in self.members:
            raise ValueError("Member not found")
        if book_id not in self.books:
            raise ValueError("Book not found")    
        else:       
            book = self.books[book_id]
        
            if self.books[book_id].is_borrowed == False:
                self.members[member_id].borrow_book(book)
                self.books[book_id].borrow()
            else:
                print(f"Book is already borrowed")

        
    def return_book(self,member_id: str, book_id: str):

        if self.books[book_id].is_borrowed == False:
            raise ValueError("Book not borrowed by this member")

        if member_id in self.members and book_id in self.books:
            book = self.books[book_id]
            if self.books[book_id].is_borrowed == True:
                self.members[member_id].return_book(book)
                self.books[book_id].return_book()
        else:
            raise ValueError("Library_return_book")
        
    def get_borrowed_books(self, member_id) -> list[Book]:

        if member_id in self.members:
            return self.members[member_id].borrowed_books
        else:
            raise ValueError("get_borrowed_books")	

library = Library()

library.add_book("B001", "The Great Gatsby", "F. Scott Fitzgerald")
library.add_book("B002", "1984", "George Orwell")
library.add_book("B003", "To Kill a Mockingbird", "Harper Lee")

# Register members
library.register_member("M001", "Alice")
library.register_member("M002", "Bob")
library.register_member("M003", "Charlie")

# Borrow books
library.borrow_book("M001", "B001")
library.borrow_book("M002", "B002")

 # Return books
library.return_book("M001", "B001")
library.return_book("M002", "B002")

library.borrow_book("M001", "B001")
try:
    library.borrow_book("M002", "B001")
except ValueError as e:
    print(e)