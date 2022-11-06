# A) This will compute the average salary of managers.

import csv  # Importing the csv file to extract data.

file = open(r"employees.csv")  # Command to open and read the csv file.

try:                                 # Applying try statement to process the file.
    csv_reader = csv.reader(file)    # Applying csv_reader to read the file.
    total = 0                        # Setting variable to compute the total.
    i = 0                            # Setting variable to iterate.
    for column in csv_reader:        # Applying for loop to iterate columns in csv file.
        if column[3] == "Manager":   # Applying if statement to choose employee type - Manager
            total += int(column[2])  # Adding the salary of Managers in the employee type column
            i += 1                   # Iterating the entries of salary with employee type: Manager
    print("The average salary of managers is", int(total / i), "dollars", ".")
    # Computing the average salary by dividing the total salary of managers by number of managers.
    # Applying the int function to get the computed output.
    # Printing the average salary.

finally:
    file.close()  # Applying finally statement to close the file.


# B) This will find the employee with the lowest salary.

import csv  # Importing the csv file to extract data.

file = open(r"employees.csv")   # Command to open and read the csv file.

try:
    csv_reader = csv.reader(file)
    row = 0
    lowest_value = int(column[2])+1
    for column in csv_reader:
        if row > 0 and int(column[2]) <= lowest_value:
            lowest_value = int(column[2])
            employee_name = column[0] + " " + column[1]
        row += 1
    print(employee_name, "has the lowest salary $", float(lowest_value), ".")
    # Applying float data type to get the lowest value.
    # Printing the employee_name and the lowest salary of the employee.

finally:
    file.close()  # Applying finally statement to close the file.
