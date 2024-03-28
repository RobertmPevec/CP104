"""
------------------------------------------------------------------------
Lab 8, Task 9
------------------------------------------------------------------------
Author: Robert Pevec
ID:     169081145
Email:  peve1145@mylaurier.ca
__updated__ = '2024-03-27'
------------------------------------------------------------------------
"""
from functions import count_frequency_value
with open("t09test.txt", "r+", encoding="utf-8") as fh:
    num = count_frequency_value(fh, 6)
    print(num)