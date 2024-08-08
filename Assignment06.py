# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   Miles Devine, 8/7/2024, Created script
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''

FILE_NAME: str = "Enrollments.json"


students: list = []  # a table of student data
menu_choice: str  # Hold the choice made by the user.

class FileProcessor:
    """
    A collection of processing layer functions that work with Json files.

    (Who, When, What)
    M. Devine, 8/7/2024, Created Class
    """
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """
        This function reads data from a file and saves it to a two-dimensional list.

        ChangeLog: (Who, When, What)
        M. Devine, 8/7/2024, Create function
        """
        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages("The file must exist before running this script...\n",e)
        except Exception as e:
            IO.output_error_messages("There was an unspecified error...\n",e)
        finally:
            if file.closed == False:
                file.close()
        return student_data


    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """
        This function writes(saves) the users inputs to a file then outputs what was saved to the file.

        ChangeLog: (Who, When, What)
        M. Devine, 8/7/2024, Created function
        return: two-dimensional list of student registration data
        """
        try:
            file = open(file_name, "w")
            json.dump(student_data, file)

            file.close()
            print("\nThe following data was saved!\n")
            for student in student_data:
                message = "{}, {}, {}"
                print(message.format(student["FirstName"],student["LastName"], student["CourseName"]))
                # print(f'Student {student["FirstName"]} '
                #       f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        except Exception as e:
            if file.closed == False:
                file.close()
            print("Error: There was a problem with writing to the file.")
            print("Please check that the file is not open by another program.")
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        return student_data


class IO:
    """
    A collection of presentation layer functions that manage user inputs and outputs.

    (Who, When, What)
    M. Devine, 8/7/2024, Created Class
    """
    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """
        This function displays error messages to the user.

        ChangeLog: (Who, When, What)
        M. Devine, 8/7/2024, Created function
        """
        print(message)
        if error is not None:
            print("----- Generic Python Error Message -----")
            print(error, error.__doc__, sep='\n')


    @staticmethod
    def output_menu(menu:str):
        """
        This function outputs the menu of options for the user to choose from.

        ChangeLog: (Who, When, What)
        M. Devine, 8/7/2024, Created function.
        """
        print("\n", menu, "\n")

    @staticmethod
    def input_menu_choice():
        """
        This function captures and returns a menu input value from the user.

        ChangeLog: (Who, When, What)
        M. Devine, 8/7/2024, Created function

        :return: a menu choice(str) from the user
        """
        m_choice = "0"
        try:
            m_choice = input("What would you like to do? ")
            if m_choice not in ("1","2","3","4"):
                print("\nI did not understand that. Please enter 1, 2, 3, or 4. ")
        except Exception as e:
                IO.output_error_messages(e.__str__())

        return m_choice

    @staticmethod
    def input_student_data(student_data: list):
        """
        This function captures the user's inputted student data.

        ChangeLog: (Who, When, What)
        M. Devine, 8/7/2024, Created function

        return: a two-dimensional list of student registration data
        """
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("\nThe first name should not contain numbers.\n")

            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("\nThe last name should not contain numbers.\n")

            course_name = input("Please enter the name of the course: ")
            student = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            student_data.append(student)
            print(f"\nYou have registered {student_first_name} {student_last_name} for {course_name}.\n")
        except ValueError as e:
            IO.output_error_messages("\nThat value was of the wrong data type.\n")
        except Exception as e:
            IO.output_error_messages("\nThere was an unspecified error. \n")
        return student_data


    @staticmethod
    def output_student_courses(student_data: list):
        """
        This function outputs the student registration data.

        ChangeLog: (Who, When, What)
        M. Devine, 8/7/2024, Created function
        :return: none
        """
        print("-" * 50)
        for student in student_data:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)

#End of function definitions

#Start the body of the text

students = FileProcessor.read_data_from_file(file_name=FILE_NAME,student_data=students) #Read the data from the file into a two-dimensional list

while (True): #Start the while loop
    IO.output_menu(menu=MENU) #Output the menu of options to the user

    menu_choice = IO.input_menu_choice() #Capture and store the user's choice

    if menu_choice == "1":
        IO.input_student_data(student_data=students) #Capture the user's inputs regarding student registration and append them to a two-dimensional list
        continue
    elif menu_choice == "2":
        IO.output_student_courses(student_data=students) #Display the current data
        continue
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students) #Save the current data to a json file
        continue
    elif menu_choice == "4":
        input("\nWaiting for you to press enter....") #Pause before exiting the program
        break #Break out of the while loop
