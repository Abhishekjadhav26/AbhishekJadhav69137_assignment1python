# Abhishek_jadhav_69137
# Assignment_5  

import csv

print("STUDENT DATA FILE READER")

file_name = input("Enter Student File Name: ")
try:

    file = open(
        file_name,
        "r"
    )

    reader = csv.DictReader(file)

    total_marks = 0
    count = 0

    highest_marks = 0
    lowest_marks = 100

    print("\nSTUDENT INFORMATION")    

    for student in reader:

        try:

            roll_no = student["RollNo"]
            name = student["Name"]
            course = student["Course"]
            grade = student["Grade"]

            attendance = int(
                student["Attendance"]
            )

            marks = int(
                student["Marks"]
            )

            print("\nStudent Record")

            print(
                "Roll Number:",
                roll_no
            )

            print(
                "Name:",
                name
            )

            print(
                "Course:",
                course
            )

            print(
                "Grade:",
                grade
            )

            print(
                "Attendance:",
                attendance
            )

            print(
                "Marks:",
                marks
            )

            total_marks += marks
            count += 1

            if marks > highest_marks:

                highest_marks = marks

            if marks < lowest_marks:

                lowest_marks = marks

        except ValueError:

            print(
                "Invalid Student Data."
            )

        except Exception:

            print(
                "Incomplete Student Record."
            )

    file.close()
    
    print("ACADEMIC SUMMARY")   

    if count > 0:

        average = total_marks / count

        print(
            "Total Students:",
            count
        )

        print(
            "Average Marks:",
            average
        )

        print(
            "Highest Marks:",
            highest_marks
        )

        print(
            "Lowest Marks:",
            lowest_marks
        )

    else:

        print(
            "Student file is empty."
        )

except FileNotFoundError:

    print(
        "Student file not found."
    )

except Exception:

    print(
        "Unexpected Error Occurred."
    )

finally:

    print(
        "\nFile operation completed."
    )