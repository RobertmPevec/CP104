"""
------------------------------------------------------------------------
Lab 8, Task 11
------------------------------------------------------------------------
Author: Robert Pevec
ID:     169081145
Email:  peve1145@mylaurier.ca
__updated__ = '2024-03-27'
------------------------------------------------------------------------
"""
from functions import find_longest
with open("t11test.txt", "r+", encoding="utf-8") as fh:
    num = find_longest(fh)
    print(num)
