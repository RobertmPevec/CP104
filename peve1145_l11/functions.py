"""
------------------------------------------------------------------------
Assignment 9, Functions
------------------------------------------------------------------------
Author: Robert Pevec
ID:     169081145
Email:  peve1145@mylaurier.ca
__updated__ = '2024-04-02'
------------------------------------------------------------------------
"""
import random


def generate_matrix_num(rows, cols, low, high, value_type):
    """
    -------------------------------------------------------
    Generates a 2D rixlist of numbers of the given type, 'float' or 'int'.
    (To generate random float number use random.uniform and to
    generate random integer number use random.randint)
    Use: matrix = generate_matrix_num(rows, cols, low, high, value_type)
    -------------------------------------------------------
    Parameters:
        rows - number of rows in the list (int > 0)
        cols - number of columns (int > 0)
        low - low value of range (float)
        high - high value of range (float > low)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        matrix - a 2D list of random numbers (2D list of float/int)
    -------------------------------------------------------
    """
    matrix = []
    for _ in range(rows):
        row = []
        for _ in range(cols):
            if value_type == "float":
                number = random.uniform(low, high)
            else:
                number = random.randint(low, high)
            row.append(number)
        matrix.append(row)
    return matrix


def print_matrix_num(matrix, value_type):
    """
    -------------------------------------------------------
    Prints the contents of a 2D list in a formatted table.
    Prints float values with 2 decimal points and prints row and
    column headings.
    Use: print_matrix_num(matrix, 'float')
    Use: print_matrix_num(matrix, 'int')
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of values (2D list)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        None.
    -------------------------------------------------------
    """
    # print("   ", end='')
    # for n in range(columns):
    #     print(f"{n:>6}", end='')
    # print()
    # for n in range(rows):
    #     print(f"{n:<3}", end='')
    #     for _ in range(columns):
    #         if value_type == "float":
    #             number = random.uniform(low, high)
    #             print(f"{number:6.2f}", end='')
    #         else:
    #             number = random.randint(low, high)
    #             print(f"{number:6}", end='')
    #     print()
    # return None
    # Get the number of rows and columns
    num_rows = len(matrix)
    num_columns = len(matrix[0]) if num_rows > 0 else 0
    column_headers = "    " + " ".join(f"{col:<4}" for col in range(num_columns)).rstrip()
    print(column_headers)
    for row_index, row in enumerate(matrix):
        row_str = f"{row_index} "
        for elem in row:
            if value_type == 'float':
                row_str += f"{elem:4.2f} "
            elif value_type == 'int':
                row_str += f"{int(elem):<4d} "
        print(row_str.rstrip())
    return None


def print_matrix_char(matrix):
    """
    -------------------------------------------------------
    Prints the contents of a 2D list of strings in a formatted table.
    Prints row and column headings.
    Use: print_matrix_char(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of strings (2D list)
    Returns:
        None.
    -------------------------------------------------------
    """
    column_headers = "  "
    num_columns = max(len(row) for row in matrix)
    for n in range(num_columns):
        column_headers += f"{n:>5}"
    print(column_headers)
    for row_index, row in enumerate(matrix):
        row_str = f" {row_index}"
        for elem in row:
            row_str += f"{elem:>5}"
        print(row_str)
    return None


def matrix_stats(matrix):
    """
    -------------------------------------------------------
    Returns statistics on a 2D list.
		Use: smallest, largest, total, average = matrix_stats(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of numbers (2D list of float/int)
    Returns:
        smallest - the smallest number in matrix (float/int)
        largest - the largest number in matrix (float/int)
        total - the total of the numbers in matrix (float/int)
        average - the average of numbers in matrix (float/int)
    -------------------------------------------------------
    """
    total = 0
    loops = 0
    smallest = float('inf')
    largest = float('-inf')
    for row in matrix:
        for col in row:
            if col < smallest:
                smallest = col
            if col > largest:
                largest = col
            loops += 1
            total += col
    average = total / loops
    return smallest, largest, total, average


def find_position(matrix):
    """
    -------------------------------------------------------
    Determines the first locations [row, column] of smallest and
    largest values in a 2D list.
    Use: s_loc, l_loc = find_position(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of numbers (2D list)
    Returns:
        s_loc - a list of of the row and column location of
            the smallest value in matrix (list of int)
        l_loc - a list of of the row and column location of
            the largest value in matrix (list of int)
    -------------------------------------------------------
    """
    smallest = float('inf')
    largest = float('-inf')
    s_loc = [0, 0]
    l_loc = [0, 0]
    for n, row in enumerate(matrix):
        for i, value in enumerate(row):
            if value < smallest:
                smallest = value
                s_loc = [n, i]
            if value > largest:
                largest = value
                l_loc = [n, i]
    return s_loc, l_loc


def matrix_transpose(matrix):
    """
    -------------------------------------------------------
    Transpose the contents of matrix. (Swap the rows and columns.)
    Use: transposed = matrix_transpose(matrix):
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list (2D list of *)
    Returns:
        transposed - the transposed matrix (2D list of *)
    ------------------------------------------------------
    """
    transposed = []
    for i in range(len(matrix[0])):
        new_row = []
        for j in range(len(matrix)):
            new_row.append(matrix[j][i])
        transposed.append(new_row)
    return transposed
