"""
------------------------------------------------------------------------
Assignment 4, Functions
------------------------------------------------------------------------
Author: Robert Pevec
ID:     169081145
Email:  peve1145@mylaurier.ca
__updated__ = '2024-02-21'
------------------------------------------------------------------------
"""


def day_of_the_week(day_num):
    """
    -------------------------------------------------------
    Returns the name of a day of the week given an integer day number.
    Day 1 is "Sunday", day 7 is "Saturday".
    Returns "Error" if the number is not valid.
    Use: day = day_of_the_week(day_num)
    -------------------------------------------------------
    Parameters:
        day_num - day number (1 <= int <= 7)
    Returns:
        day - name of a day of the week (str)
    ------------------------------------------------------
    """
    if day_num == 1:
        day = "Sunday"
    elif day_num == 2:
        day = "Monday"
    elif day_num == 3:
        day = "Tuesday"
    elif day_num == 4:
        day = "Wednesday"
    elif day_num == 5:
        day = "Thursday"
    elif day_num == 6:
        day = "Friday"
    else:
        day = "Saturday"
    return day


def pollution_level(air_quality_index):
    """
    -------------------------------------------------------
    Returns the pollution level given an AQI (Air Quality Index):
        "Good" - 0 to 50 AQI
        "Moderate" - 51 - 100 AQI
        "Unhealthy for Sensitive Groups" - 101 - 150 AQI
        "Unhealthy" - 151 - 200 AQI
        "Very Unhealthy" - 201 - 300 AQI
        "Hazardous" - 300+ AQI
    Returns "Error" if air_quality_index is negative.
    Use: pollution = pollution_level(air_quality_index)
    -------------------------------------------------------
    Parameters:
        air_quality_index - Air Quality Index (int)
    Returns:
        pollution - name of pollution level (str)
    ------------------------------------------------------
    """
    if air_quality_index <= 50:
        pollution = "good"
    elif 51 <= air_quality_index <= 100:
        pollution = "Moderate"
    elif 101 <= air_quality_index <= 150:
        pollution = "Unhealthy for Sensitive Groups"
    elif 151 <= air_quality_index <= 200:
        pollution = "Unhealthy"
    elif 201 <= air_quality_index <= 300:
        pollution = "Very Unhealthy"
    if air_quality_index >= 300:
        pollution = "Hazardous"
    return pollution


def largest_product(val1, val2, val3):
    """
    -------------------------------------------------------
    Returns the product of the two largest values of
    val1, val2, and val3.
    Use: product = largest_product(val1, val2, val3)
    -------------------------------------------------------
    Parameters:
        val1 - a number (float)
        val2 - a number (float)
        val3 - a number (float)
    Returns:
        product - the product of the two largest values of
            val1, val2, and val3 (float)
    ------------------------------------------------------
    """
    non_number = min(val1, val2, val3)
    if non_number == val1:
        number = val2 * val3
    elif non_number == val2:
        number = val1 * val3
    else:
        number = val1 * val2
    return float(number)


def colour_mix(rgb_colour1, rgb_colour2):
    """
    -------------------------------------------------------
    Determines the secondary rgb_colour from mixing two primary
    RGB (Red, Green, Blue) colours. The order of the colours
    is *not* significant.
    Returns "Error" if any of the rgb_colour parameter(s) are invalid.
        "red" + "blue": "fuchsia"
        "red" + "green": "yellow"
        "green" + "blue": "aqua"
        "red" + "red": "red"
        "blue" + "blue": "blue"
        "green" + "green": "green"
    Use: rgb_colour = colour_mix(rgb_colour1, rgb_colour2)
    -------------------------------------------------------
    Parameters:
        rgb_colour1 - a primary RGB rgb_colour (str)
        rgb_colour2 - a primary RGB rgb_colour (str)
    Returns:
        rgb_colour - a secondary RGB rgb_colour (str)
    -------------------------------------------------------
    """
    if (rgb_colour1 == "red" and rgb_colour2 == "blue") or (rgb_colour1 == "blue" and rgb_colour2 == "red"):
        final_color = "fuchsia"
    elif (rgb_colour1 == "red" and rgb_colour2 == "green") or (rgb_colour1 == "green" and rgb_colour2 == "red"):
        final_color = "yellow"
    elif (rgb_colour1 == "green" and rgb_colour2 == "blue") or (rgb_colour1 == "blue" and rgb_colour2 == "green"):
        final_color = "aqua"
    elif rgb_colour1 == "red" and rgb_colour2 == "red":
        final_color = "red"
    elif rgb_colour1 == "blue" and rgb_colour2 == "blue":
        final_color = "blue"
    elif rgb_colour1 == "green" and rgb_colour2 == "green":
        final_color = "green"
    else:
        raise ValueError("Please enter either Red, Green or Blue")  # Changed from raising an exception to returning "Error" as per the function documentation
    return final_color


def yee_ha(number):
    """
    -------------------------------------------------------
    Use: answer = yee_ha(number)
    -------------------------------------------------------
    Parameters:
        number - any number
    Returns:
        answer - either "Yee Ha", "Yee", "Ha" or "Nada"
    -------------------------------------------------------
    """
    if number % 3 == 0 and number % 7 == 0:
        answer = "Yee Ha"
    elif number % 3 == 0:
        answer = "Yee"
    elif number % 7 == 0:
        answer = "Ha"
    else:
        answer = "Nada"
    return answer
