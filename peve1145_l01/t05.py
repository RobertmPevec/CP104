"""
------------------------------------------------------------------------
Assignment 1, Task 5
------------------------------------------------------------------------
Author: Robert Pevec
ID:     169081445
Email:  peve1145@mylaurier.ca
__updated__ = '2024-01-16'
------------------------------------------------------------------------
"""
# inputs
principle = float(input("Principle: $"))
interest = float(input("Interest (%): "))
numb_of_years = int(input("Number of years: "))
compound_rate = int(input("Number of times interest compounded per year: "))
# equation
equation = principle * (1 + interest / 100 / compound_rate)**(compound_rate * numb_of_years)
# output
print(f"Balance: ${equation:.2f}")
