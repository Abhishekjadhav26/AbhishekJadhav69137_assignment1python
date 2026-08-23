class Library:
    def __init__(self, library_name):
        self.library_name = library_name;
        self.books_collection = [];
        self.members_collection = [];

    def add_book(self, book):
        self.books_collection.append(book);
        print(f"{book.title} added to library.");

    def remove_book(self, book):
        if book in self.books_collection:
            self.books_collection.remove(book);
            print(f"{book.title} removed from library.");
        else:
            print("Book not found.");

    def register_member(self, member):
        self.members_collection.append(member);
        print(f"{member.member_name} registered successfully.");

    def search_book(self, search_value):
        found = False;

        for book in self.books_collection:

            if book.title == search_value or book.author == search_value or book.isbn == search_value:
                print(book);
                found = True;

        if found == False:
            print("Book not found.");

    def issue_book(self, book, member):
        if book in self.books_collection and member in self.members_collection:
            member.borrow_book(book);
        else:
            print("Book or member not found in library.");

    def accept_return(self, book, member, overdue_days):
        if member in self.members_collection:
            member.return_book(book, overdue_days);
        else:
            print("Member not found.");

    def display_all_books(self):
        print("\n= ALL BOOKS =");

        for book in self.books_collection:
            print(book);

    def display_available_books(self):
        print("\n= AVAILABLE BOOKS =");

        for book in self.books_collection:
            if book.check_availability():
                print(book);

    def display_issued_books(self):
        print("\n= ISSUED BOOKS =");

        for book in self.books_collection:
            if book.check_availability() == False:
                print(book);

    def display_members(self):
        print("\n= MEMBERS =");

        for member in self.members_collection:
            member.display_details();
            print();

    def generate_report(self):
        
        print(f"LIBRARY REPORT - {self.library_name}");        

        print(f"Total Books: {len(self.books_collection)}");
        print(f"Total Members: {len(self.members_collection)}");

        print("\nMember Borrowing Statistics:");

        for member in self.members_collection:
            print(
                f"{member.member_name} - Borrowed Books: "
                f"{member.get_borrowed_book_count()}"
            );