"""
------------------------------------------------------------------------
Lab 8, Task 14
------------------------------------------------------------------------
Author: Robert Pevec
ID:     169081145
Email:  peve1145@mylaurier.ca
__updated__ = '2024-03-27'
------------------------------------------------------------------------
"""
from functions import file_copy_n
with open("t14test.txt", "r", encoding="utf-8") as fh_1:
    # Open the destination file for appending
    with open("t11test.txt", "a", encoding="utf-8") as fh_2:
        # Call the function to copy 5 lines from fh_1 to fh_2
        file_copy_n(fh_1, fh_2, 5)
