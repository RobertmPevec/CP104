"""
------------------------------------------------------------------------
Assignment 5, Functions
------------------------------------------------------------------------
Author: Robert Pevec
ID:     169081145
Email:  peve1145@mylaurier.ca
__updated__ = '2024-03-10'
------------------------------------------------------------------------
"""
from collections import Counter


# def most_common(lst):
#     return max(set(lst), key=lst.count)
#
#
# def winner():
#     portal = ""
#     score = []
#     while True:
#         name = input("Enter the winning team:")
#         if name == portal:
#             break
#         else:
#             score.append(name)
#     top_two = Counter(score).most_common(2)
#     return top_two
def winner():
    """
    -------------------------------------------------------
    Calculates the total wins for two teams, 'purple' <str> and
    'gold' <str>. The user enters a series of strings, and once
    they decide to finish, they must press 'Enter' or input
    an empty string on their keyboard.
    -------------------------------------------------------
    Use: blue, grey = winner()
    -------------------------------------------------------
    Parameters:
        None
    Returns:
        purple - <str> number of purple wins
        gold - <str>  number of gold wins
    ------------------------------------------------------
    """

    blue = 0
    grey = 0
    finish = False

    while finish == False:
        team = input("Enter the winning team: ")

        if team == "blue":
            blue += 1

        elif team == "grey":
            grey += 1

        elif team == "":
            finish = True

    return blue, grey


def is_prime_number(number):
    """
    -------------------------------------------------------
    Determines if number is a prime number.
    Use: is_prime = is_prime_number(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int > 1)
    Returns:
        is_prime - True if number is prime, False otherwise (bool)
    -----------------------------------------------------
    """
    n = number - 1
    if number == 1:
        is_prime = False
    else:
        is_prime = True
    while is_prime is True and n > 1:
        if (number % n) == 0:
            is_prime = False
        n -= 1
    return is_prime


def interest_data(principal_amount, interest_rate, payment):
    """
    -------------------------------------------------------
    Prints a table of monthly interest and payments on a loan.
    Use: interest_data(principal_amount, interest_rate, payment)
    -------------------------------------------------------
    Parameters:
        principal_amount - original value of a loan (float > 0)
        interest_rate - yearly interest interest_rate as a % (float >= 0)
        payment - the monthly payment (float > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    balance = principal_amount
    month = 1
    print(f"Principle: ${principal_amount:,.2f}")
    print(f"Interest Rate: {interest_rate}%")
    print(f"Monthly Payment: ${payment:,.2f}")
    print(f"""----------------------------------
Month Interest   Payment   Balance
----------------------------------""")
    while balance > 0:
        interest = balance * (interest_rate / 1200)
        balance = balance + interest - payment
        if balance < 0:
            payment += balance
            balance = 0
        print(f"{month:>5} {interest:>8.2f} {payment:>9,.2f} {balance:>9,.2f}")
        month += 1
    return None
