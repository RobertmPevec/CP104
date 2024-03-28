"""
------------------------------------------------------------------------
Lab 8, Task 7
------------------------------------------------------------------------
Author: Robert Pevec
ID:     169081145
Email:  peve1145@mylaurier.ca
__updated__ = '2024-03-27'
------------------------------------------------------------------------
"""
from functions import append_max_num
with open("t07test.txt", "r+", encoding="utf-8") as fh:
    num = append_max_num(fh)
    print(num)
