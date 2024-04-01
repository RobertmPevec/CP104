"""
------------------------------------------------------------------------
Assignment 9, Task 5
------------------------------------------------------------------------
Author: Robert Pevec
ID:     169081145
Email:  peve1145@mylaurier.ca
__updated__ = '2024-03-29'
------------------------------------------------------------------------
"""
from functions import student_data
fh = open("t05test.txt", "r", encoding="utf-8")
result = student_data(fh)
print(result)
fh.close()
