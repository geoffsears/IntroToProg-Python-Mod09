# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# GSEARS, 12-05-2019, Copied contents of Listing 13 into Main.py
# GSEARS, 12-05-2019, constructed main while loop
# GSEARS, 12-05-2019, diagnosed nesting Russian Doll syndrome with imported list
# GSEARS, 12-05-2019, fixed error correction for non-numeric Emp_ID entry
# GSEARS, 12-06-2019, removed DataClasses import as it is unneeded. (moved to ProcessingClasses
#           read_data_from_file method.
# ------------------------------------------------------------------------ #


#Data
dataFile = "EmployeeData.txt"  # Name of Data File used by Script
lstTable = [] #container for Employee objects once created
new_emp = "" #variable used for passing new employee data to Employee Class

if __name__ == "__main__":
    from ProcessingClasses import FileProcessor as Fp # import FileProcessor to read/write to datafile
    from IOClasses import EmployeeIO as Eio # provide user input and display options for employee list
else:
    raise Exception("This file was not created to be imported") # test to ensure we are in main script.

# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of employee objects when script starts
# Show user a menu of options
# Get user's menu option choice
    # Show user current data in the list of employee objects
    # Let user add data to the list of employee objects
    # let user save current data to file
    # Let user exit program
lstTable = Fp.read_data_from_file(dataFile)
while True:
    Eio.print_menu_items()
    choice = Eio.input_menu_options()
    if choice == "1":
        Eio.print_current_list_items(lstTable)
        continue
    elif choice == "2":
        new_emp = Eio.input_employee_data()
        if new_emp == "":
            continue
        else:
            lstTable.append(new_emp)
        continue
    elif choice == "3":
        Fp.save_data_to_file(dataFile, lstTable)
        continue
    elif choice == "4":
        print("Thank you for using the Employee Data List Manager. Good Bye")
        print()
        break
    else:
        "You need to make a selection between 1 and 4."



# Main Body of Script  ---------------------------------------------------- #
