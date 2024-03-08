"""
------------------------------------------------------------------------
Lab 6, Functions
------------------------------------------------------------------------
Author: Robert Pevec
ID:     169081145
Email:  peve1145@mylaurier.ca
__updated__ = '2024-02-18'
------------------------------------------------------------------------
"""


def sum_odd(num):
    """
    -------------------------------------------------------
    Sums and returns the total of all odd numbers from 1 to num (inclusive).
    Use: total = sum_odd(num)
    -------------------------------------------------------
    Parameters:
        num - an integer (int > 0)
    Returns:
        total - sum of all odd numbers from 1 to num (int)
    ------------------------------------------------------
    """
    total = 0
    for n in range(1, num + 1, 2):
        total += n
    return total


def draw_triangle(height, char):
    """
    -------------------------------------------------------
    Prints a triangle of height characters using
    the char character.
    Use: draw_triangle(height, char)
    -------------------------------------------------------
    Parameters:
        height - number of characters high (int > 0)
        char - the character to draw with (str, len() == 1)
    Returns:
        None
    ------------------------------------------------------
    """
    numb = 1
    for n in range(height):
        spaces = height - n - 1
        print(" " * spaces + char * numb)
        numb += 2
    return None
#     numb = 1
#     max_width = (2 * height) - 1
#     triangle = ""
#     for n in range(height):
#         triangle += (" " * max_width) + (numb * char) + "\n"
#         max_width -= 1
#         numb += 2
#     return triangle


def bottles_of_beer(n):
    """
    -------------------------------------------------------
    Prints n verses of the song "99 Bottles of Beer on the Wall".
    Use: bottles_of_beer(n)
    -------------------------------------------------------
    Parameters:
        n - number of verses of the song to print (int > 0)
    Returns:
        None
    ------------------------------------------------------
    """
#     for _ in range(n):
#         if n > 2:
#             print(f"""
# {n} bottles of beer on the wall, {n} bottles of beer.
# Take one down, pass it around, {n - 1} bottles of beer on the wall.
# --
# """)
#             n -= 1
#         elif n == 2:
#             print(f"""
# {n} bottles of beer on the wall, {n} bottles of beer.
# Take one down, pass it around, {n - 1} bottle of beer on the wall.
# """)
#             n -= 1
#         else:
#             print(f"""
# 1 bottle of beer on the wall, 1 bottle of beer.
# Take one down, pass it around, no more bottles of beer on the wall!
# """)
#             n -= 1
    for i in range(n, 0, -1):
        bottles = f"{i} bottle{'s' if i != 1 else ''}"
        next_bottles = f"{i - 1} bottle{'s' if i - 1 != 1 else ''}" if i - 1 > 0 else "no more bottles"
        print(f"""
{bottles} of beer on the wall, {bottles} of beer.
Take one down, pass it around, {next_bottles} of beer on the wall.
--""")
        return None


def retirement(age, salary, increase):
    """
    -------------------------------------------------------
    Calculates and prints a table of how much a worker
    earns between age and retirement at 65.
    Use: retirement(age, salary, increase)
    -------------------------------------------------------
    Parameters:
        age - worker's current age (int > 0)
        salary - worker's current salary (float > 0)
        increase - percent increase in salary per year (float >= 0)
    Returns:
        None
    ------------------------------------------------------
    """
    # increase = increase / 100
    # print("Age         Salary\n------------------")
    # for i in range(age, 65, 1):
    #     salary = (salary * increase) + salary
    #     age += 1
    #     print(f"{age:<5} {salary:>12,.2f}")
    # return None
    increase = increase / 100
    print("Age         Salary")
    print("------------------")

    for current_age in range(age, 66):  # Loop until 65 included
        if current_age != age:  # Apply increase after the first year shown
            salary += (salary * increase)
        print(f"{current_age:<5} {salary:12,.2f}")

    return None


def statistics(n):
    """
    -------------------------------------------------------
    Asks a user to enter n values, then calculates and returns
    the minimum, maximum, total, and average of those values.
    Use: minimum, maximum, total, average = statistics(n)
    -------------------------------------------------------
    Parameters:
        n - number of values to process (int > 0)
    Returns:
        minimum - smallest of n values (float)
        maximum - largest of n values (float)
        total - total of n values (float)
        average - average of n values (float)
    ------------------------------------------------------
    """
    # total = 0
    # numbers = []
    # for i in range(n):
    #     value = float(input("Enter a Value: "))
    #     numbers.append(value)
    #     total += value
    # minimum = min(numbers)
    # maximum = max(numbers)
    # average = total / n
    # return minimum, maximum, total, average
    total = 0
    minimum = float('inf')  # Initialize minimum as infinity
    maximum = float('-inf')  # Initialize maximum as negative infinity

    for _ in range(n):
        value = float(input("Enter a Value: "))
        # Compare value to find minimum and maximum
        if value < minimum:
            minimum = value
        if value > maximum:
            maximum = value
        total += value

    average = total / n
    return minimum, maximum, total, average
