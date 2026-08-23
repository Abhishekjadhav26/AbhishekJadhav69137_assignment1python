# Abhishek_jadhav_69137
# Assignment_7  

import sqlite3


def create_connection():

    return sqlite3.connect(
        "student_db.db"
    )


def create_table():

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(
        student_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        date_of_birth TEXT NOT NULL,
        gender TEXT NOT NULL,
        course TEXT NOT NULL,
        department TEXT NOT NULL,
        semester INTEGER NOT NULL,
        roll_number TEXT NOT NULL,
        enrollment_number TEXT NOT NULL UNIQUE,
        admission_date TEXT NOT NULL,
        email TEXT NOT NULL,
        mobile_number TEXT NOT NULL,
        address TEXT NOT NULL,
        city TEXT NOT NULL,
        state TEXT NOT NULL,
        postal_code TEXT NOT NULL,
        guardian_name TEXT NOT NULL,
        guardian_contact TEXT NOT NULL,
        emergency_contact TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()


def register_student():

    print("\n STUDENT REGISTRATION ")

    first_name = input("First Name : ")
    last_name = input("Last Name : ")
    date_of_birth = input("Date of Birth : ")
    gender = input("Gender : ")
    course = input("Course Name : ")
    department = input("Department : ")
    semester = int(input("Semester : "))
    roll_number = input("Roll Number : ")
    enrollment_number = input("Enrollment Number : ")
    admission_date = input("Admission Date : ")
    email = input("Email Address : ")
    mobile_number = input("Mobile Number : ")
    address = input("Residential Address : ")
    city = input("City : ")
    state = input("State : ")
    postal_code = input("Postal Code : ")
    guardian_name = input("Guardian Name : ")
    guardian_contact = input("Guardian Contact Number : ")
    emergency_contact = input("Emergency Contact Number : ")

    if first_name == "" or last_name == "" or enrollment_number == "":

        print("Mandatory Fields Cannot Be Empty")

    else:

        conn = create_connection()

        cursor = conn.cursor()

        cursor.execute("""
        SELECT *
        FROM students
        WHERE enrollment_number=?
        """,
        (enrollment_number,))

        student = cursor.fetchone()

        if student:

            print("Enrollment Number Already Exists")

        else:

            cursor.execute("""
            INSERT INTO students(
                first_name,
                last_name,
                date_of_birth,
                gender,
                course,
                department,
                semester,
                roll_number,
                enrollment_number,
                admission_date,
                email,
                mobile_number,
                address,
                city,
                state,
                postal_code,
                guardian_name,
                guardian_contact,
                emergency_contact
            )
            VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            """,
            (
                first_name,
                last_name,
                date_of_birth,
                gender,
                course,
                department,
                semester,
                roll_number,
                enrollment_number,
                admission_date,
                email,
                mobile_number,
                address,
                city,
                state,
                postal_code,
                guardian_name,
                guardian_contact,
                emergency_contact
            ))

            conn.commit()

            print("Student Registered Successfully")

        conn.close()


def view_all_students():

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students"
    )

    rows = cursor.fetchall()

    conn.close()

    print("\n===== ALL STUDENTS =====")

    for row in rows:

        print(row)

    print("\nTotal Students :", len(rows))


def search_student_by_id():

    student_id = int(
        input("Enter Student ID : ")
    )

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM students
    WHERE student_id=?
    """,
    (student_id,))

    row = cursor.fetchone()

    conn.close()

    if row:

        print("\nStudent Record")
        print(row)

    else:

        print("Student Not Found")


def search_student_by_name():

    name = input(
        "Enter Student Name : "
    )

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM students
    WHERE first_name LIKE ?
    OR last_name LIKE ?
    """,
    ('%' + name + '%',
     '%' + name + '%'))

    rows = cursor.fetchall()

    conn.close()

    if rows:

        print("\nSearch Results")

        for row in rows:

            print(row)

    else:

        print("Student Not Found")


def update_student():

    student_id = int(
        input("Enter Student ID : ")
    )

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM students
    WHERE student_id=?
    """,
    (student_id,))

    student = cursor.fetchone()

    if student:

        print("\nEnter Updated Information")

        first_name = input("First Name : ")
        last_name = input("Last Name : ")
        mobile_number = input("Mobile Number : ")
        email = input("Email Address : ")
        address = input("Address : ")
        department = input("Department : ")
        semester = int(input("Semester : "))
        course = input("Course : ")

        cursor.execute("""
        UPDATE students
        SET first_name=?,
            last_name=?,
            mobile_number=?,
            email=?,
            address=?,
            department=?,
            semester=?,
            course=?
        WHERE student_id=?
        """,
        (
            first_name,
            last_name,
            mobile_number,
            email,
            address,
            department,
            semester,
            course,
            student_id
        ))

        conn.commit()

        print("Student Information Updated")

    else:

        print("Student Not Found")

    conn.close()


def delete_student():

    student_id = int(
        input("Enter Student ID : ")
    )

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM students
    WHERE student_id=?
    """,
    (student_id,))

    student = cursor.fetchone()

    if student:

        print(student)

        confirm = input(
            "Are You Sure You Want To Delete? (yes/no) : "
        )

        if confirm == "yes":

            cursor.execute("""
            DELETE FROM students
            WHERE student_id=?
            """,
            (student_id,))

            conn.commit()

            print("Student Record Deleted")

        else:

            print("Deletion Cancelled")

    else:

        print("Student Not Found")

    conn.close()


def department_report():

    department = input(
        "Enter Department : "
    )

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM students
    WHERE department LIKE ?
    """,
    ('%' + department + '%',))

    rows = cursor.fetchall()

    conn.close()

    print("\n===== DEPARTMENT REPORT =====")

    for row in rows:

        print(row)

    print("Total Students :", len(rows))


def course_report():

    course = input(
        "Enter Course : "
    )

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM students
    WHERE course LIKE ?
    """,
    ('%' + course + '%',))

    rows = cursor.fetchall()

    conn.close()

    print("\n===== COURSE REPORT =====")

    for row in rows:

        print(row)

    print("Total Students :", len(rows))


def student_count_report():

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students"
    )

    students = cursor.fetchall()

    print("\n===== STUDENT COUNT REPORT =====")

    print("Total Students :", len(students))

    print("\nDepartment-wise Count")

    cursor.execute("""
    SELECT department, COUNT(*)
    FROM students
    GROUP BY department
    """)

    departments = cursor.fetchall()

    for row in departments:

        print(row)

    print("\nCourse-wise Count")

    cursor.execute("""
    SELECT course, COUNT(*)
    FROM students
    GROUP BY course
    """)

    courses = cursor.fetchall()

    for row in courses:

        print(row)

    conn.close()


def menu():

    create_table()

    while True:
       
        print("STUDENT DATABASE MANAGEMENT SYSTEM")

        print("1. Register New Student")
        print("2. View All Students")
        print("3. Search Student by ID")
        print("4. Search Student by Name")
        print("5. Update Student Information")
        print("6. Delete Student Record")
        print("7. Department-wise Report")
        print("8. Course-wise Report")
        print("9. Student Count Report")
        print("10. Exit")

        choice = input(
            "Enter Your Choice : "
        )

        if choice == "1":

            register_student()

        elif choice == "2":

            view_all_students()

        elif choice == "3":

            search_student_by_id()

        elif choice == "4":

            search_student_by_name()

        elif choice == "5":

            update_student()

        elif choice == "6":

            delete_student()

        elif choice == "7":

            department_report()

        elif choice == "8":

            course_report()

        elif choice == "9":

            student_count_report()

        elif choice == "10":

            print("Exiting Student Database Management System")
            break

        else:

            print("Invalid Choice")


if __name__ == "__main__":

    menu()