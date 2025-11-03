#!/usr/bin/env python3
# Created by: Patrick
# Created on: 10/30/2025
# This program determines if a year is a leap year
def main():

    # Ask the user for a year
    year_string = input("Enter a year: ")

    try:
        year = int(year_string)

        # calculates if the year is a leap year
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    is_leap_year = True
                else:
                    is_leap_year = False
            else:
                is_leap_year = True
        else:
            is_leap_year = False

        # Displays if the year is a leap year or not
        if is_leap_year:
            print("This a leap year.")
        else:
            print("This not a leap year.")

    except ValueError:
        print("Invalid input. Please enter a valid year.")


if __name__ == "__main__":
    main()
