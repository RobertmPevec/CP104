"""
------------------------------------------------------------------------
Assignment 7, Functions
------------------------------------------------------------------------
Author: Robert Pevec
ID:     169081145
Email:  peve1145@mylaurier.ca
__updated__ = '2024-03-14'
------------------------------------------------------------------------
"""


def list_of_factors(number):
    """
    -------------------------------------------------------
    Takes an integer greater than 0 as a parameter and returns
    a list of its factors, excluding the number itself.
    Use: list = list_factors(number)
    -------------------------------------------------------
    Parameters:
    - number (int): The integer for which to find the factors.
        It should be greater than 0.
    Returns:
    - factors (list): A list of factors for which the number
        corresponds with. It should have at least 2 numbers.
    Use: list_of_factors
    -------------------------------------------------------
    """
    factors = []
    for i in range(1, number):
        if number % i == 0:
            factors.append(i)
    return factors


def list_of_positives():
    """
    -------------------------------------------------------
    Gets a list of positive numbers from a user.
    Negative numbers are ignored. Enter 0 to stop entries.
    Use: number_list = list_of_positives()
    -------------------------------------------------------
    Returns:
        number_list - A list of positive integers (list of int)
    ------------------------------------------------------
    """
    number_list = []
    while True:
        numb = int(input("Enter a positive number: "))
        if numb == 0:
            break
        elif numb > 0:
            number_list.append(numb)
    return number_list


def find_indexes(numbers, target_number):
    """
    -------------------------------------------------------
    Finds the indexes of target_number in numbers.
    Use: index_list = find_indexes(numbers, target_number)
    -------------------------------------------------------
    Parameters:
        numbers - list of values (list)
        target_number - value to look for in num_list (*)
    Returns:
        index_list - list of indexes of target_number (list of int)
    -------------------------------------------------------
    """
    index_list = []
    add_numb = 0
    while True:
        if target_number in numbers:
            numb = numbers.index(target_number)
            index_list.append(numb + add_numb)
            del numbers[numb]
            add_numb += 1
        else:
            break
    return index_list


def list_subtraction(minuend, subtrahend):
    """
    -------------------------------------------------------
    Alters the contents of minuend so that it does not contain
    any values in subtrahend.
    i.e., the values in the first list that appear in the second list
    are removed from the first list.
    Use: list_subtraction(minuend, subtrahend)
    -------------------------------------------------------
    Parameters:
        minuend - a list of values (list)
        subtrahend - a list of values to not include in difference (list)
    Returns:
        None
    ------------------------------------------------------
    """
    minuend[:] = [value for value in minuend if value not in subtrahend]
    return None


def check_sorted(numbers):
    """
    -------------------------------------------------------
    Determines whether a list is sorted.
    Use: in_order, index = check_sorted(numbers)
    -------------------------------------------------------
    Parameters:
        numbers - a list of numbers (list)
    Returns:
        in_order - True if numbers is sorted, False otherwise (bool)
        index - index of first value not in order,
            -1 if in_order is True (int)
    ------------------------------------------------------
    """
    length = len(numbers)
    n = 1
    return_statement = True, -1
    for i in range(0, length - 1):
        numb_1 = numbers[i]
        numb_2 = numbers[n]
        if numb_1 > numb_2:
            return_statement = False, 1
        n += 1
    return return_statement
