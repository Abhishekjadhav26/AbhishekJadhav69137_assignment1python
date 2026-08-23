class Book:
    def __init__(self, book_id, title, author, isbn, available_copies):
        self.book_id = book_id; 
        self.title = title; 
        self.author = author; 
        self.isbn = isbn; 
        self.__available_copies = available_copies; 

    def issue_book(self):
        if self.__available_copies > 0:
            self.__available_copies = self.__available_copies - 1;
            return True;
        else:
            print("Book is not available.");
            return False;

    def return_book(self):
        self.__available_copies = self.__available_copies + 1;

    def check_availability(self):
        if self.__available_copies > 0:
            return True;
        else:
            return False;

    def get_available_copies(self):
        return self.__available_copies;

    def set_available_copies(self, copies):
        if copies >= 0:
            self.__available_copies = copies;
        else:
            raise ValueError("Available copies cannot be negative.");

    def __str__(self):
        return f"Book ID: {self.book_id}, Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Available Copies: {self.__available_copies}";

    def __repr__(self):
        return f"Book(book_id={self.book_id}, title={self.title}, author={self.author}, isbn={self.isbn}, available_copies={self.__available_copies})";

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.isbn == other.isbn;
        return False;

    def __add__(self, other):
        return self.__available_copies + other.__available_copies if isinstance(other, Book) else NotImplemented;