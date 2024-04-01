"""
------------------------------------------------------------------------
Assignment 9, Functions
------------------------------------------------------------------------
Author: Robert Pevec
ID:     169081145
Email:  peve1145@mylaurier.ca
__updated__ = '2024-03-29'
------------------------------------------------------------------------
"""


def file_header(file_handle, count):
    """
    -------------------------------------------------------
    Prints first count lines of file_handle. Line numbering starts at 0.
    If length of file is shorter than count, stops printing after
    last line of file.
    Use: file_header(file_handle, count)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
        count - number of lines to print (int > 0)
    Returns:
        None
    -------------------------------------------------------
    """
    total = 0
    while total < count:
        line = file_handle.readline().strip()
        print(line)
        total += 1
    return None


def extract_integers(file_handle):
    """
    -------------------------------------------------------
    Extracts positive integers from a file into a list of integers.
    Numbers are comma-delimited. Non-numeric tokens are ignored.
    Use: number_list = extract_integers(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
    Returns:
        number_list - a list of integers from file_handle (list of int)
    -------------------------------------------------------
    """
    number_list = []
    for n in file_handle:
        line = n.strip().split(',')
        for number in line:
            try:
                numb = int(number)
                if numb > 0:
                    number_list.append(numb)
            except ValueError:
                continue
    return number_list


def text_stats(file_handle):
    """
    -------------------------------------------------------
    Evaluates the contents of a file by counting upper-case letters,
    lower-case letters, digits, white-spaces (including end-of-line
    characters), and remaining characters.
    Use: ucount, lcount, dcount, wcount, rcount = text_stats(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
    Returns:
        ucount - The number of upper-case letters in the file (int)
        lcount - The number of lower-case letters in the file (int)
        dcount - The number of digits in the file (int)
        wcount - The number of white-space characters in the file (int)
        rcount - The number of remaining characters in the file (int)
    -------------------------------------------------------
    """
    ucount = 0
    lcount = 0
    dcount = 0
    wcount = 0
    rcount = 0
    for n in file_handle:
        for character in n:
            if character.isupper():
                ucount += 1
            elif character.islower():
                lcount += 1
            elif character.isdigit():
                dcount += 1
            elif character.isspace():
                wcount += 1
            else:
                rcount += 1
    return ucount, lcount, dcount, wcount, rcount


def add_numbers(fh_read, fh_write):
    """
    -------------------------------------------------------
    Adds line numbers to a file. Contents of fh_write contain contents
    of fh_read where every line has line numbers added to the beginning
    of the line in the format [number]. Line numbering starts at 0.
    Put a single space after the line number.
    Use: add_numbers(fh_read, fh_write)
    -------------------------------------------------------
    Parameters:
        fh_read - file to read (file - open for reading)
        fh_write - file to write (file - open for writing)
    Returns:
        None
    -------------------------------------------------------
    """
    for index, line in enumerate(fh_read):
        fh_write.write(f"[{index}] {line}")


def student_data(file_handle):
    """
    -------------------------------------------------------
    Get information from a file of file_handle and grades.
    Use: l_id, h_id, avg = student_data(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - student information file in the format
            surname,forename,id,mark (file - open for reading)
    Returns:
        l_id - the id of the student with the lowest mark (str)
        h_id - the id of the student with the highest mark (str)
        avg - the average mark (float)
    -------------------------------------------------------
    """
    avg = 0
    lowest_mark = 101
    highest_mark = -1
    l_id = ""
    h_id = ""
    total_students = 0
    for line in file_handle:
        total_students += 1
        updated_line = line.strip().split(',')
        mark = float(updated_line[3])
        avg += mark
        if lowest_mark > mark:
            lowest_mark = mark
            l_id = updated_line[2]
        if highest_mark < mark:
            highest_mark = mark
            h_id = updated_line[2]
    avg /= total_students
    return l_id, h_id, avg
