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
from functions import extract_integers
fh = open("t02test.txt", "r", encoding="utf-8")
result = extract_integers(fh)
print(result)
fh.close()
