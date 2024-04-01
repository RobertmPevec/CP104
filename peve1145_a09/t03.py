"""
------------------------------------------------------------------------
Assignment 9, Task 2
------------------------------------------------------------------------
Author: Robert Pevec
ID:     169081145
Email:  peve1145@mylaurier.ca
__updated__ = '2024-03-29'
------------------------------------------------------------------------
"""
from functions import text_stats
fh = open("t03test.txt", "r", encoding="utf-8")
result = text_stats(fh)
print(result)
fh.close()
