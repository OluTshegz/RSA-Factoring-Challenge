#!/usr/bin/python3
"""instructs the OS to find and execute
    the Python 3 interpreter located
    in the env directory
    within the system path
    """

import sys
import time
"""required modules to import"""


def factorize(number):
    """a function that takes number as argument"""
    for x in range(2, int(number**0.5) + 1):
        """a simple loop to check for factors up to the square root of number"""
        if number % x == 0:
            print("{:d}={:d}*{:d}".format(number, x, number//x))


def main(filename):
    """a function that takes filename(./tests/test00)
        as argument and prints their factorizations
        """
    try:
        with open(filename, 'r') as file:
            """opens the file using python file handling"""
            numbers = file.read().splitlines()
    except FileNotFoundError:
        """FileError handling"""
        print("Usage: factors <filename>")
        """Error: File '{filename}' not found. Ensure tests/test00 is present!"""
        sys.exit(1)
    except Exception as e:
        """Other exception handling"""
        print(f"{e}, fail!")
        """Error: An unexpected error occurred - {e}"""
    for num in numbers:
        """This loop iterates through each number in the list obtained from the file."""
        try:
            num = int(num)
            """converts the string representation of the number to an integer"""
            if num <= 1:
                """Invalid natural number"""
                print(f"Error: {num} is not a valid natural number greater than 1.")
                continue
            num_1, num_2 = factorize(num)
            print("{:d}={:d}*{:d}".format(num, num_1, num_2))
        except ValueError:
            """ValueError handling"""
            print(f"Error: '{num}' is not a valid natural number.")
        except Exception as e:
            """Other exception handling"""
            print(f"Error: An unexpected error occurred - {e}")

if __name__ == "__main__":
    """checks if the script is being run as the main program (__name__ is set to "__main__")."""
    if len(sys.argv) != 2:
        """checks if the correct number of command-line arguments is provided.
            If not, it prints a usage message, sleeps for 5 seconds and exits.
            """
        print("Usage: factors <filename>")
        time.sleep(5)
        sys.exit(1)

    filename = sys.argv[1]
    """extracts the filename from the command-line arguments"""
    main(filename)
    """calls the main function with that filename."""
