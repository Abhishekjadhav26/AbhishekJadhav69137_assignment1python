from abc import ABC, abstractmethod;

class LibraryUser(ABC):
    def __init__(self, member_id, member_name):
        self.__member_id = member_id; 
        self.member_name = member_name; 
        self.__outstanding_fine = 0; 
        self.__borrowed_book_count = 0; 
        self.borrowed_books = [];
        self.borrowing_history = [];

    @abstractmethod
    def borrow_book(self, book):
        pass;

    @abstractmethod
    def return_book(self, book, overdue_days):
        pass;

    @abstractmethod
    def calculate_fine(self, overdue_days):
        pass;

    def get_member_id(self):
        return self.__member_id;

    def get_outstanding_fine(self):
        return self.__outstanding_fine;

    def set_outstanding_fine(self, fine):
        if fine >= 0:
            self.__outstanding_fine = fine;
        else:
            raise ValueError("Fine cannot be negative.");

    def get_borrowed_book_count(self):
        return self.__borrowed_book_count;

    def set_borrowed_book_count(self, count):
        if count >= 0:
            self.__borrowed_book_count = count;
        else:
            raise ValueError("Borrowed book count cannot be negative.");

    def pay_fine(self, amount):
        if amount > 0 and amount <= self.__outstanding_fine:
            self.__outstanding_fine = self.__outstanding_fine - amount;
            print(f"Fine payment of {amount} successful.");
            print(f"Remaining Fine: {self.__outstanding_fine}");
        else:
            print("Invalid fine payment amount.");

    def display_details(self):
        print(f"Member ID: {self.__member_id}");
        print(f"Member Name: {self.member_name}");
        print(f"Borrowed Books: {self.__borrowed_book_count}");
        print(f"Outstanding Fine: {self.__outstanding_fine}");

    def display_borrowing_history(self):
        print(f"\nBorrowing History of {self.member_name}:");

        if len(self.borrowing_history) == 0:
            print("No borrowing history.");
        else:
            for book in self.borrowing_history:
                print(book.title);