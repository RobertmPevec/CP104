"""
------------------------------------------------------------------------
Assignment 3, Functions
------------------------------------------------------------------------
Author: Robert Pevec
ID:     169081145
Email:  peve1145@mylaurier.ca
__updated__ = '2024-02-17'
------------------------------------------------------------------------
"""


def footage_to_acres(square_feet):
    """
    -------------------------------------------------------
    Converts square footage to acres.
    Use: acres = footage_to_acres(square_feet)
    -------------------------------------------------------
    Parameters:
        square_feet - area in square feet (float >= 0)
    Returns:
        acres - square_footage in acres (float)
    ------------------------------------------------------
    """
    acres = 43560
    acres = square_feet / acres
    return acres


def lawn_mowing(width, length, speed):
    """
    -------------------------------------------------------
    Determines how long it takes to mow a rectangular lawn.
    Use: time = lawn_mowing(width, length, speed)
    -------------------------------------------------------
    Parameters:
        width - width of a lawn in metres (float > 0)
        length - length of a lawn in metres (float > 0)
        speed - square metres cut per minute (float > 0)
    Returns:
        time_minutes - time required to mow the lawn (float)
    ------------------------------------------------------
    """
    time = width * length / speed
    return time


def date_extraction(date_number_format):
    """
    -------------------------------------------------------
    Extracts the year, month, and day from a date number in the format MMDDYYYY.
    Use: year, month, day = date_extraction(date_number_format)
    -------------------------------------------------------
    Parameters:
        date_number_format - a date number in the format MMDDYYYY (int > 0)
    Returns:
        year - year portion of date_number (int)
        month - month portion of date_number (int)
        day - day portion of date_number (int)
    ------------------------------------------------------
    """
    year = date_number_format % 10000
    month = date_number_format // 1000000
    day = date_number_format // 10000 % 100
    return year, month, day


def fraction_multiplier(number1, denom1, number2, denom2):
    """
    -------------------------------------------------------
    Multiplies two fractions together and returns the results
    Use: num, denom, product = fraction_multiplier(number1, denom1, number2, denom2)
    -------------------------------------------------------
    Parameters:
        number1 - numerator of the first fraction (int)
        denom1 - denominator of the first fraction (int)
        number2 - numerator of the second fraction (int)
        denom2 - denominator of the second fraction (int)
    Returns:
        num - numerator of the resulting fraction (int)
        denom - denominator of the resulting fraction  (int)
        product - numerator divided by denominator (float)
    ------------------------------------------------------
    """
    product = (number1 / denom1) * (number2 / denom2)
    num = number1 * number2
    denom = denom1 * denom2
    return num, denom, product


def falling_distance(time):
    """
    -------------------------------------------------------
    Calculates distance an object has fallen due to gravity given
    the time it is fallen.
    Use: distance = falling_distance(falling_time)
    -------------------------------------------------------
    Parameters:
        time - time object has fallen in seconds (int >= 0)
    Returns:
        distance - distance object has fallen in metres (float)
    -------------------------------------------------------
    """
    g = 9.8
    distance = 0.5 * g * time ** 2
    return distance
