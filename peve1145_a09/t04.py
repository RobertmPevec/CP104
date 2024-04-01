"""
------------------------------------------------------------------------
Assignment 9, Task 4
------------------------------------------------------------------------
Author: Robert Pevec
ID:     169081145
Email:  peve1145@mylaurier.ca
__updated__ = '2024-03-29'
------------------------------------------------------------------------
"""
from functions import add_numbers

# Using 'with' statements to ensure files are properly closed after operations
with open("t04test.txt", "r", encoding="utf-8") as fileread, \
     open("t04testwrite.txt", "w", encoding="utf-8") as filewrite:
    # Assuming 'add_numbers' processes the files and doesn't return a value
    add_numbers(fileread, filewrite)