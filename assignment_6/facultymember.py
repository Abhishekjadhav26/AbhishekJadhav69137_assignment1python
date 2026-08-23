import libraryuser as LU;

class FacultyMember(LU.LibraryUser):
    def __init__(self, member_id, member_name):
        super().__init__(member_id, member_name);
        self.borrow_limit = 5;
        self.grace_period = 5;

    def borrow_book(self, book):
        if self.get_borrowed_book_count() < self.borrow_limit:

            if book.check_availability():
                if book.issue_book():
                    self.borrowed_books.append(book);
                    self.borrowing_history.append(book);

                    self.set_borrowed_book_count(
                        self.get_borrowed_book_count() + 1
                    );

                    print(f"{book.title} issued to {self.member_name}.");
            else:
                print("Book is not available.");

        else:
            print("Faculty borrowing limit reached.");

    def return_book(self, book, overdue_days):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book);
            book.return_book();

            self.set_borrowed_book_count(
                self.get_borrowed_book_count() - 1
            );

            fine = self.calculate_fine(overdue_days);

            self.set_outstanding_fine(
                self.get_outstanding_fine() + fine
            );

            print(f"{book.title} returned successfully.");
            print(f"Fine: {fine}");

        else:
            print("This book was not borrowed by the member.");

    def calculate_fine(self, overdue_days):
        if overdue_days > self.grace_period:
            return (overdue_days - self.grace_period) * 1;
        else:
            return 0;

    def __str__(self):
        return f"FacultyMember(member_id={self.get_member_id()}, member_name={self.member_name}, borrowed_books={self.get_borrowed_book_count()}, outstanding_fine={self.get_outstanding_fine()})";