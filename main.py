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
    factors = []
    max_iterations = 1718944270642558716715
    for x in range(2, int(number**0.5) + 1):
        if x > max_iterations:
            break
        if number % x == 0:
            factors.append((x, number // x))
            if len(factors) >= 2:
                break
    if factors:
        for factor in factors:
            print("{:d}={:d}*{:d}".format(number, factor[1], factor[0]))
        return factors[0]
    else:
        print("{:d} is a prime number.".format(number))
        return None


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
        """Error: File '{filename}' not found. Ensure ./test00 is present!"""
        sys.exit(1)
    except Exception as e:
        """Other exception handling"""
        print(f"{e}, fail!")
        """Error: An unexpected error occurred - {e}"""
    for num in numbers:
        """loop iterating each number in the list obtained from the file."""
        try:
            num = int(num)
            """converts the string to an integer"""
            if num <= 1 or num > 1718944270642558716715:
                """Invalid natural number"""
                print(f"""Error: {num} is not a valid natural number
                      greater than 1 OR""")
                print(f"""Skipping factorization for {num}
                      as it exceeds the threshold.""")
                continue
            factor_pair = factorize(num)
            if factor_pair is not None:
                num_1, num_2 = factor_pair
        except ValueError:
            """ValueError handling"""
            print(f"Error: '{num}' is not a valid natural number.")
        except Exception as e:
            """Other exception handling"""
            print(f"Error: An unexpected error occurred - {e}")


if __name__ == "__main__":
    """checks if the script is being run as the main program
        (__name__ is set to "__main__")."""
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
