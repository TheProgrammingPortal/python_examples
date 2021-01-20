input_year = int(input("Enter a year:"))

# Method - 1 -> using If condition with logic

def is_leap(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True

    return False

if is_leap(input_year):
    print("It is a leap year")
else:
    print("It is not a leap year")


# Method - 2 -> using Python built In method from Calendar module

import calendar

if calendar.isleap(input_year):
    print("It is a leap year")
else:
    print("It is not a leap year")









