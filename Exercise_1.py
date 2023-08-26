#########################################################################################
#                                    Exercise 1
#########################################################################################

from datetime import datetime, date

# User Given input for their date of birth
user_dob = input("Enter your date of birth (mm/dd/yyyy): ")

#try-except block is used to handle the case where the user enters an invalid date format.
#enables us to more effectively manage issues that may happen at runtime and improve user experience.
try:
    # Convert the input string to a date object
    dob = datetime.strptime(user_dob, "%m/%d/%Y").date()

    # Get today's date
    today = date.today()

    # Check if the user has had their birthday this year
    birthday_thisyear = (today.month, today.day) >= (dob.month, dob.day)

    # Calculate the user's age
    user_age = today.year - dob.year - int(not birthday_thisyear)

    # Output the user's age
    print("Your age is:", user_age)

    # Output European format Date
    dob_europe = dob.strftime("%d/%m/%Y")
    print("Date of birth (European format):", dob_europe)

except ValueError:
    # Handle invalid input
    print("Invalid date format, please enter in the format mm/dd/yyyy.")