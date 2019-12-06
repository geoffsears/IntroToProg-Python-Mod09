# ---------------------------------------------------------- #
# Title: ProcessingClasses.py
# Description: A module of multiple processing classes
# ChangeLog (Who,When,What):
# GSEARS, 2019-12-05, Copied contents of LIsting07.py to this script for later use.
# GSEARS, 2019-12-06, added call to DataClasses class to read_data_from_file class to enable
#       employee object creation from imported data.
# ---------------------------------------------------------- #
if __name__ == "__main__":
#    from DataClasses import Employee as Emp
    raise Exception("This file is not meant to ran by itself")

class FileProcessor:
    """Processes data to and from a file and a list of objects:

    methods:
        save_data_to_file(file_name,list_of_objects):

        read_data_from_file(file_name): -> (a list of objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
    """

    @staticmethod
    def save_data_to_file(file_name: str, list_of_objects: list):
        """ Write data to a file from a list of object rows

        :param file_name: (string) with name of file
        :param list_of_objects: (list) of objects data saved to file
        :return: (bool) with status of success status
        """
        success_status = False
        try:
            file = open(file_name, "w")
            for row in list_of_objects:
                file.write(row.__str__() + "\n")
            file.close()
            success_status = True
        except Exception as e:
            print("There was a general error!")
            print(e, e.__doc__, type(e), sep='\n')
        return success_status

    @staticmethod
    def read_data_from_file(file_name: str):
        """ Reads data from a file into a list of object rows

        :param file_name: (string) with name of file
        :return: (list) of object rows
        """
        from DataClasses import Employee as Emp
        list_of_rows = []
        try:
            file = open(file_name, "r")
            for line in file:
                data = line.split(",")
                try:
                    row = Emp(data[0].strip(),data[1].strip(),data[2].strip())
                    list_of_rows.append(row)
                except: #if there is an error creating object then continue to close file connection.
                    continue
            file.close()
        except Exception as e:
            print("There was a general error!")
            print(e, e.__doc__, type(e), sep='\n')
        return list_of_rows