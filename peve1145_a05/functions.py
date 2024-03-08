"""
------------------------------------------------------------------------
Assignment 5, Functions
------------------------------------------------------------------------
Author: Robert Pevec
ID:     169081145
Email:  peve1145@mylaurier.ca
__updated__ = '2024-03-04'
------------------------------------------------------------------------
"""


def factorial_calculator(number):
    """
    -------------------------------------------------------
    Calculates and returns the factorial of number.
    Use: product = factorial_calculator(number)
    -------------------------------------------------------
    Parameters:
        number - number to factorial (int > 0)
    Returns:
        product - number! (int)
    ------------------------------------------------------
    """
    product = 1
    for n in range(number):
        product *= n + 1
    return product


def calories_burned(per_min, minutes):
    """
    -------------------------------------------------------
    Calculates and returns calories burned
    Use: total_cals = calories_burned(per_min, minutes):
    -------------------------------------------------------
    Parameters:
        per_min - calories burned per min (int > 0)
        minutes - length of time calories burned (int > 0)
    Returns:
        total_cals - burned calories / minutes worked (int)
    ------------------------------------------------------
    """
    total_cals = 0
    for n in range(5, minutes + 1, 5):
        total_cals += 5 * per_min
        print(f"{n:>2}  {total_cals:>3.1f}")
    return None


def arrow_down(rows):
    """
    -------------------------------------------------------
    Calculates and prints downward arrow with specific amount of rows
    -------------------------------------------------------
    Parameters:
        rows - amount of rows in downward arrow
    Returns:
        use - arrow_down
    ------------------------------------------------------
    """

    letter = "#"
    space = " "
    total_spaces = 0
    if rows // 2 == 0:
        middle_spaces = rows + 2
    else:
        middle_spaces = rows + 1
    for n in range(rows - 1):
        print((space * total_spaces) + letter + (space * middle_spaces) + letter)
        total_spaces += 1
        middle_spaces -= 2
    print((total_spaces * space) + letter)
    return None


def multiplication_table(start_num, stop_num):
    """
    -------------------------------------------------------
    Prints a multiplication table for values from start_num to stop_num.
    Use: multiplication_table(start_num, stop_num)
    -------------------------------------------------------
    Parameters:
        start_num - the range start value (int)
        stop_num - the range stop value (int)
    Returns:
        None
    ------------------------------------------------------
    """
    largest_number = stop_num * stop_num
    width = len(str(largest_number))
    noreturn = 1
    for n in range(start_num, stop_num + 1):
        if noreturn == 1:
            space = "     "
        else:
            space = ""
        print(f" {space}{n:>{width}}", end="")
        noreturn = 0
    print("\n", "    ", "-" * (width * (stop_num - start_num + 1) + (stop_num - start_num)))
    for row in range(start_num, stop_num + 1):
        print(f" {row:>{width - 1}} |", end="")
        for col in range(start_num, stop_num + 1):
            print(f" {row * col:>{width}}", end="")
        print()
    return None


def range_total(start, increment, count):
    """
    -------------------------------------------------------
    Uses a for loop to sum values from start by increment.
    Use: total = range_total(start, increment, count)
    -------------------------------------------------------
    Parameters:
        start - the range start value (int)
        increment - the range increment (int)
        count - the number of values in the range (int)
    Returns:
        total - the sum of the range (int)
    ------------------------------------------------------
    """
    total = 0
    for n in range(start, count * increment, increment):
        total += n
    return total
