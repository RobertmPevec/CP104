"""
------------------------------------------------------------------------
Lab 4, Functions
------------------------------------------------------------------------
Author: Robert Pevec
ID:     169081445
Email:  peve1145@mylaurier.ca
__updated__ = '2024-02-05'
------------------------------------------------------------------------
"""
import math


def diameter(radius):

    """
    -------------------------------------------------------
    Calculates and returns diameter of a circle.
    Use: diam = diameter(radius)
    -------------------------------------------------------
    Parameters:
        radius - radius of a circle (float >= 0)
    Returns:
        diam - diameter of a circle (float)
    ------------------------------------------------------
    """
    if not isinstance(radius, (float, int)):
        raise ValueError("Please enter a number for the radius.")
    if radius < 0:
        raise ValueError("Please enter a positive number for the radius.")
    diam = radius * 2
    return diam


def circumference(radius):
    """
    -------------------------------------------------------
    Calculates and returns circumference of a circle.
    Use: circ = circumference(radius)
    -------------------------------------------------------
    Parameters:
        radius - radius of a circle (float >= 0)
    Returns:
        circ - circumference of a circle (float)
    ------------------------------------------------------
    """
    if not isinstance(radius, (float, int)):
        raise ValueError("Please enter a number for the radius.")
    if radius < 0:
        raise ValueError("Please enter a positive number for the radius.")
    circ = 2 * math.pi * radius
    return circ


def area(radius):
    """
    -------------------------------------------------------
    Calculates and returns area of a circle.
    Use: ar = area(radius)
    -------------------------------------------------------
    Parameters:
        radius - radius of a circle (float >= 0)
    Returns:
        ar - area of a circle (float)
    ------------------------------------------------------
    """
    if not isinstance(radius, (float, int)):
        raise ValueError("Please enter a number for the radius.")
    if radius < 0:
        raise ValueError("Please enter a positive number for the radius.")
    ar = math.pi * radius**2
    return ar


def square_pyramid(base, height):
    """
    -------------------------------------------------------
    Calculates and returns the slant height, area, and
    volume of a square pyramid given the base and perpendicular
    height.
    Use: sh, area, vol = square_pyramid(base, height)
    -------------------------------------------------------
    Parameters:
        base - length of the base of the pyramid (float > 0)
        height - perpendicular height of the pyramid (float > 0)
    Returns:
        sh - slant height of the square pyramid (float)
        area - area of the square pyramid (float)
        vol - volume of the square pyramid (float)
    ------------------------------------------------------
    """
    if base <= 0 or height <= 0:
        raise ValueError("Please enter a positive number for the base/height.")
    else:
        sh = math.sqrt((base / 2) ** 2 + (height ** 2))
        area = base ** 2 + 2 * base * math.sqrt(base ** 2 / 4 + height ** 2)
        vol = base ** 2 * (height / 3)
        return sh, area, vol


def right_triangle(adjacent, opposite):
    """
    -------------------------------------------------------
    Calculates and returns the hypotenuse, perimeter, and
    area of a right triangle given two non-hypotenuse sides.
    Use: hyp, per, area = right_triangle(adjacent, opposite)
    -------------------------------------------------------
    Parameters:
        adjacent - length of side right triangle (float > 0)
        opposite - length of side right triangle (float > 0)
    Returns:
        hyp - hypotenuse of the triangle (float)
        per - perimeter of the triangle (float)
        area - area of the triangle (float)
    ------------------------------------------------------
    """
    hyp = math.sqrt((adjacent ** 2) + (opposite ** 2))
    per = adjacent + opposite + hyp
    area = adjacent * opposite / 2
    return hyp, per, area


def total_change(nickels, dimes, quarters, loonies, toonies):

    """
    -------------------------------------------------------
    Calculates the total value of a set of coins in dollars.
    Each coin is worth:
        nickel:  $0.05
        dime:    $0.10
        quarter: $0.25
        loonie:  $1.00
        toonie:  $2.00
    Use: total = total_change(nickels, dimes, quarters,
        loonies, toonies)
    -------------------------------------------------------
    Parameters:
        nickels - number of nickels (int >= 0)
        dimes - number of dimes (int >= 0)
        quarters - number of quarters (int >= 0)
        loonies - number of loonies (int >= 0)
        toonies - number of toonies (int >= 0)
    Returns:
        total - total value of coins (float)
    -------------------------------------------------------
    """
    if nickels < 0 or dimes < 0 or quarters < 0 or loonies < 0 or toonies < 0:
        raise ValueError("Please enter a non-negative number for all values.")
    NICKEL = 0.05
    DIME = 0.10
    QUARTER = 0.25
    LOONIE = 1.00
    TOONIE = 2.00
    total = (NICKEL * nickels) + (DIME * dimes) + (QUARTER * quarters) + (LOONIE * loonies) + (TOONIE * toonies)
    return total


def population(size, births, deaths, immigrants, years):
    """
    -------------------------------------------------------
    Calculates future population given various factors.
    Use: new_size = population(size, births, deaths, immigrants, years)
    -------------------------------------------------------
    Parameters:
       size - current population (int >= 0)
       births - average seconds between births (int >= 0)
       deaths - average seconds between deaths (int >= 0)
       immigrants - average seconds between immigrations (int >= 0)
       years - years to calculate new population (int > 0)
    Returns:
       new_size - new population size (int)
    -------------------------------------------------------
    """
    if size < 0 or births < 0 or deaths < 0 or immigrants < 0 or years < 0:
        raise ValueError("Please enter a non-negative number for all values.")
    SECONDS_PER_YEAR = 31536000
    births = SECONDS_PER_YEAR / births
    deaths = SECONDS_PER_YEAR / deaths
    immigrants = SECONDS_PER_YEAR / immigrants
    new_size = round(size + (births - deaths + immigrants) * years)
    return new_size


def time_values(seconds):
    """
    -------------------------------------------------------
    Returns seconds in different formats.
    Use: days, hours, minutes = time_values(seconds)
    -------------------------------------------------------
    Parameters:
        seconds - total seconds (int >= 0)
    Returns:
        days - number of days in total_seconds (int >= 0)
        hours - number of hours in total_seconds (int >= 0)
        minutes - number of minutes in total_seconds (int >= 0)
    -------------------------------------------------------
    """
    if seconds < 0:
        raise ValueError("Please enter a positive value for seconds")
    SECONDS_PER_DAY = 86400
    SECONDS_PER_HOUR = 3600
    SECONDS_PER_MINUTE = 60
    days = seconds // SECONDS_PER_DAY
    hours = seconds // SECONDS_PER_HOUR
    minutes = seconds // SECONDS_PER_MINUTE
    return days, hours, minutes
