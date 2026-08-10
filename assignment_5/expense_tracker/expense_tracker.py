# Abhishek_jadhav_69137
# Assignment_5  
import csv

while True:
   
    print("EXPENSE TRACKER")
    
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Expense Summary")
    print("4. Exit")

    choice = input("Enter Choice: ")

    try:

        if choice == "1":

            file = open(
                "expenses.csv",
                "a",
                newline=""
            )

            writer = csv.writer(file)

            date = input(
                "Enter Date: "
            )

            category = input(
                "Enter Category: "
            )

            description = input(
                "Enter Description: "
            )

            amount = float(
                input(
                    "Enter Amount: "
                )
            )

            writer.writerow([
                date,
                category,
                description,
                amount
            ])

            file.close()

            print(
                "Expense Added Successfully"
            )

        elif choice == "2":

            file = open(
                "expenses.csv",
                "r"
            )

            reader = csv.DictReader(file)

            print("\nEXPENSE HISTORY")
            

            for expense in reader:

                print("\nDate:",
                      expense["Date"])

                print(
                    "Category:",
                    expense["Category"]
                )

                print(
                    "Description:",
                    expense["Description"]
                )

                print(
                    "Amount:",
                    expense["Amount"]
                )

            file.close()

        elif choice == "3":

            file = open(
                "expenses.csv",
                "r"
            )

            reader = csv.DictReader(file)

            total_expense = 0
            count = 0
            category_total = {}

            for expense in reader:

                amount = float(
                    expense["Amount"]
                )

                category = expense[
                    "Category"
                ]

                total_expense += amount
                count += 1

                if category in category_total:

                    category_total[
                        category
                    ] += amount

                else:

                    category_total[
                        category
                    ] = amount

            file.close()
            
            print("EXPENSE SUMMARY")
            
            print(
                "Total Transactions:",
                count
            )

            print(
                "Total Expenses:",
                total_expense
            )

            print(
                "\nCATEGORY WISE EXPENSES"
            )

            for category in category_total:

                print(
                    category,
                    ":",
                    category_total[
                        category
                    ]
                )

        elif choice == "4":

            print(
                "Expense Tracker Closed"
            )

            break

        else:

            raise ValueError(
                "Invalid Menu Option"
            )

    except FileNotFoundError:

        print(
            "Expense File Not Found."
        )

    except ValueError as error:

        print(
            "ValueError:",
            error
        )

    except Exception:

        print(
            "Unexpected Error Occurred."
        )

    finally:

        print(
            "Operation Completed."
        )