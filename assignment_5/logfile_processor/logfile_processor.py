# Abhishek_jadhav_69137
# Assignment_5  

print("LOG FILE PROCESSOR")

file_name = input("Enter Log File Name:")
try:

    file = open(
        file_name,
        "r"
    )

    total_logs = 0
    info_count = 0
    warning_count = 0
    error_count = 0
    invalid_count = 0

    for line in file:

        log = line.strip()

        if log != "":

            total_logs += 1

            if "INFO" in log:

                info_count += 1

            elif "WARNING" in log:

                warning_count += 1

            elif "ERROR" in log:

                error_count += 1

                print(
                    "Critical Event:",
                    log
                )

            else:

                invalid_count += 1
    file.close()

    
    print("LOG SUMMARY")
    
    print(
        "Total Records:",
        total_logs
    )

    print(
        "Information Logs:",
        info_count
    )

    print(
        "Warning Logs:",
        warning_count
    )

    print(
        "Error Logs:",
        error_count
    )

    print(
        "Invalid Logs:",
        invalid_count
    )

    if total_logs == 0:

        print(
            "Log file is empty."
        )

except FileNotFoundError:

    print(
        "Log file not found."
    )

except Exception:

    print(
        "Unexpected Error Occurred."
    )

finally:

    print(
        "Log processing completed."
    )