"""
------------------------------------------------------------------------
Lab 8, Task 2
------------------------------------------------------------------------
Author: Robert Pevec
ID:     169081145
Email:  peve1145@mylaurier.ca
__updated__ = '2024-03-27'
------------------------------------------------------------------------
"""
from functions import customer_by_id
fh = open("t02test.txt", "r", encoding="utf-8")
result = customer_by_id(fh, '45432')
print(result)
fh.close()