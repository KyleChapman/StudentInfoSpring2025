# Author:   Kyle Chapman
# Created:  May 29, 2025
# Modified: June 3, 2025
# Description:
# Collects and validates some student information and then prints it.

# Declarations
MIN_PROGRAM_NAME = 9
MAX_PROGRAM_NAME = 100
MIN_SEMESTERS = 2
MAX_SEMESTERS = 6
SIN_DIGITS = 9

# Boolean flag.
is_valid = False

# Input
while not is_valid:
    # Get the first name as a non-blank string.
    first_name = input("Enter your first name: ").strip()

    # Check that first name is not blank.
    if first_name != "":
        is_valid = True
    else:
        # First name is blank.
        print("Error: You must enter a name.")

# Get the last name as a string.
last_name = input("Enter your last name: ").strip()

is_valid = False

while not is_valid:

    # Get the program from a list? Or get them to type it?
    program_name = input("Enter the name of your program: ").strip()

    # Check the length of the program name as typed in.
    if len(program_name) >= MIN_PROGRAM_NAME and len(program_name) <= MAX_PROGRAM_NAME:
        is_valid = True
    else:
        # Program name is too short or too long.
        print("Error: Your program name must be between",MIN_PROGRAM_NAME,"and",MAX_PROGRAM_NAME,"characters in length.")

is_valid = False

while not is_valid:

    # Use a try block to allow for the code to fail.
    try:

        # Get the semesters to graduate as number between 2 and 6.
        semesters_to_graduate = float(input("Enter the number of semesters until you graduate, and assume you're actually going to pass things: "))
        
        # Since it's a number, we can now check the range.
        if not (MIN_SEMESTERS <= semesters_to_graduate <= MAX_SEMESTERS):
            # Semesters to graduate is out-of-range.
            print("Error: Semesters to graduate must be between " + str(MIN_SEMESTERS) + " and " + str(MAX_SEMESTERS) + ".")
        else:
            is_valid = True
    except:
        # Semesters to graduate is not a number.
        print("Error: Semesters to graduate must be a number.")

is_valid = False

while not is_valid:
    # Get the Social Insurance Number as a 9-digit whole number.
    social_insurance_number = input("Enter your social insurance number (SIN): ").replace(" ","")

    # Check if the SIN is 9 numeric digits.
    if len(social_insurance_number) == SIN_DIGITS and social_insurance_number.isnumeric():
        is_valid = True
    else:
        # SIN is invalid.
        print("Error: Social insurance number must be",SIN_DIGITS,"numeric digits.")

# At this point, if is_valid is True, all inputs are valid!

# Process
# There is no processing. :)

# Output

# Output the first and last name.
print("\nName:\t" + first_name + " " + last_name)
# Output the Program
print("Program:\t" + program_name)
# Output the Semesters to Graduate
print("Semesters to Graduate:\t" + str(semesters_to_graduate))
# Output the Social Insurance Number (SIN)
print("SIN:\t" + social_insurance_number)

# Confirm close.
input("\nPress Enter to end the program....")