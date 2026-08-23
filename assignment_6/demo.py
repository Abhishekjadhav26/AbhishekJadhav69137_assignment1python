# Abhishek_jadhav_69137
# Assignment_6  

import book;
import library;
import studentmember as SM;
import facultymember as FM;
import guestmember as GM;


library1 = library.Library("City Library");

book1 = book.Book(
    101,
    "Python Programming",
    "Dr Doom",
    "BN101",
    2
);

book2 = book.Book(
    102,
    "Data Structures",
    "Iron Man",
    "BN102",
    1
);

book3 = book.Book(
    103,
    "Database Systems",
    "Thor",
    "BN103",
    1
);

# Add Books
library1.add_book(book1);
library1.add_book(book2);
library1.add_book(book3);

# Member Objects
student = SM.StudentMember(201, "Abhishek");
faculty = FM.FacultyMember(202, "Kapil");
guest = GM.GuestMember(203, "Samay");

# Register Members
library1.register_member(student);
library1.register_member(faculty);
library1.register_member(guest);

# Display Books
library1.display_all_books();

# Search Book
print("\n= SEARCH BOOK =");
library1.search_book("Python Programming");

# Issue Books
print("\n= ISSUE BOOKS =");
library1.issue_book(book1, student);
library1.issue_book(book2, faculty);
library1.issue_book(book3, guest);

# Available Books
library1.display_available_books();

# Member Details
library1.display_members();

# Polymorphism
print("\n= FINE CALCULATION =");
print(f"Student Fine: {student.calculate_fine(10)}");
print(f"Faculty Fine: {faculty.calculate_fine(10)}");
print(f"Guest Fine: {guest.calculate_fine(10)}");

# Return Books
print("\n= RETURN BOOK =");
library1.accept_return(book1, student, 5);
library1.accept_return(book2, faculty, 10);
library1.accept_return(book3, guest, 3);

# Borrowing History
student.display_borrowing_history();
faculty.display_borrowing_history();
guest.display_borrowing_history();

# Magic Method str
print("\n= MAGIC METHOD __str__ =");
print(book1);
print(student);

# Magic Method __eq__
print("\n= MAGIC METHOD __eq__ =");

book4 = book.Book(
    104,
    "Advanced Python",
    "Loki",
    "BN101",
    3
);

print(book1 == book4);

# Magic Method add
print("\n= MAGIC METHOD __add__ =");
print(book1 + book2);


library1.generate_report();