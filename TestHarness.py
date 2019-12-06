# ---------------------------------------------------------- #
# Title: TestHarness.py
# Description: A main module for testing
# ChangeLog (Who,When,What):
# GSEARS,2019-12-05,Copied Listing 8 into TestHarness.py script
# GSEARS,2019-12-05, Modfied import statements to import new Python files instead of Listing files.
# ---------------------------------------------------------- #

if __name__ == "__main__":
    from DataClasses import Person as Per
    from DataClasses import Employee as Emp
    from ProcessingClasses import FileProcessor as Fp
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported")

# Test data module
objP1 = Per("Bob", "Smith")
objP2 = Per("Sue", "Jones")
lstTableP = [objP1, objP2]
for row in lstTableP:
    print(row.to_string(), type(row))

# Test data module (Employee Class)
objP1 = Emp(1, "Bob", "Smith")
objP2 = Emp(2, "Sue", "Jones")
lstTableE = [objP1, objP2]
for row in lstTableE:
    print(row.to_string(), type(row))

# Test processing module
Fp.save_data_to_file("PersonData.txt", lstTableP)
lstFileData = Fp.read_data_from_file("PersonData.txt")
lstTableP.clear()
for row in range(len(lstFileData)):
    print(row.first_name, row.last_name)


# Test processing module (Employee)
Fp.save_data_to_file("EmployeeData.txt", lstTableE)
lstFileData = Fp.read_data_from_file("EmployeeData.txt")
lstTableE.clear()
for row in lstFileData:
    print(row.employee_id,row.first_name,row.last_name)


# Test IO classes
Eio.print_menu_items()
Eio.print_current_list_items(lstTableP)
Eio.print_current_list_items(lstTableE)
print(Eio.input_employee_data())
print(Eio.input_menu_options())
