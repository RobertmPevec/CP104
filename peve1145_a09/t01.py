"""
------------------------------------------------------------------------
Assignment 9, Task 1
------------------------------------------------------------------------
Author: Robert Pevec
ID:     169081145
Email:  peve1145@mylaurier.ca
__updated__ = '2024-03-29'
------------------------------------------------------------------------
"""
from functions import file_header
file_handle = open("t01test.txt", "r", encoding="utf-8")
file_header(file_handle, 5)
file_handle.close()
