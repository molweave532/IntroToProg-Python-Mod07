# ------------------------------------------------- #
# Title: HW07 - error handling
# Description: A brief description of error handling
# ChangeLog: (Who, When, What)
# Molly Weaver, 02/27/21, Created Script
# ------------------------------------------------- #

try:
    # write a test case here
    intOne = int(input("Please enter an integer from 1 to 10: "))
except ValueError:
    # then tell the user there was an error
    print("That's not what I'm looking for!  I need an integer.")
except Exception as error:
    print("That was unexpected!")
    print(error)
else:
    try:
        # look to see if the integer is outside the expected range
        if intOne < 1 or intOne > 10:
            raise Exception
    except Exception:
            # tell the user there was an error
            (print("That is outside the expected range!"))
    else:
        # no errors encountered!
        print("You entered: ", intOne)
finally:
    # do this every time
    print("Goodbye!")
