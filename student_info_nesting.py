# Author:   Kyle Chapman
# Date:     May 29, 2025
# Description:
# Collects and validates some student information and then prints it.

# Declarations
MIN_PROGRAM_NAME = 9
MAX_PROGRAM_NAME = 100
MIN_SEMESTERS = 2
MAX_SEMESTERS = 6
SIN_DIGITS = 9

# Input
# Get the first name as a non-blank string.
first_name = input("Enter your first name: ")

# Check that first name is not blank.
if first_name != "":
    # Get the last name as a string.
    last_name = input("Enter your last name: ")

    # Get the program from a list? Or get them to type it?
    program_name = input("Enter the name of your program: ")

    # Check the length of the program name as typed in.
    if len(program_name) >= MIN_PROGRAM_NAME and len(program_name) <= MAX_PROGRAM_NAME:
        # Get the semesters to graduate as a whole number between 2 and 6.
        semesters_to_graduate = input("Enter the number of semesters until you graduate, including the current semester, and assume you're actually going to pass things: ")

        # Check if semesters to graduate is a number.
        if semesters_to_graduate.isnumeric():
            semesters_to_graduate = int(semesters_to_graduate)
            # Since it's a number, we can now check the range.
            if MIN_SEMESTERS <= semesters_to_graduate <= MAX_SEMESTERS:
                
                # Get the Social Insurance Number as a 9-digit whole number.
                social_insurance_number = input("Enter your social insurance number (SIN): ")

                # Check if the SIN is 9 numeric digits.
                if len(social_insurance_number) == SIN_DIGITS and social_insurance_number.isnumeric():

                    # At this point, all inputs are valid!

                    # Process
                    # There is no processing. :)

                    # Output
                    # Output the first and last name.
                    print("Name:\t" + first_name + " " + last_name)
                    # Output the Program
                    print("Program:\t" + program_name)
                    # Output the Semesters to Graduate
                    print("Semesters to Graduate:\t" + str(semesters_to_graduate))
                    # Output the Social Insurance Number (SIN)
                    print("SIN:\t" + social_insurance_number)

                else:
                    # SIN is invalid.
                    print("Error: Social insurance number must be",SIN_DIGITS,"numeric digits.")
            else:
                # Semesters to graduate is out-of-range.
                print("Error: Semesters to graduate must be",MIN_SEMESTERS,"and",MAX_SEMESTERS,".")
        else:
            # Semesters to graduate is not a number.
            print("Error: Semesters to graduate must be a whole number.")
    else:
        # Program name is too short or too long.
        print("Error: Your program name must be between",MIN_PROGRAM_NAME,"and",MAX_PROGRAM_NAME,"characters in length.")
else:
    # First name is blank.
    print("You must enter a name.")

# Confirm close.
input("\nPress Enter to end the program....")