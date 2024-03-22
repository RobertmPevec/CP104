"""
------------------------------------------------------------------------
Assignment 8, Functions
------------------------------------------------------------------------
Author: Robert Pevec
ID:     169081145
Email:  peve1145@mylaurier.ca
__updated__ = '2024-03-21'
------------------------------------------------------------------------
"""


def insert_spaces(sentence):
    """
    -------------------------------------------------------
    Create a new sentence with added space between words. Words start
    with upper-case characters.
    Use: spaced = insert_spaces(sentence)
    -------------------------------------------------------
    Parameters:
        sentence - sentence that represents a sentence in which all the
            words are run together (no spaces), but the first character
            of each word is uppercase. sentence has at least one
            character (str)
    Returns:
        spaced - new sentence in which the words are separated
            by spaces and only the first word starts with
            an uppercase character (str)
    -------------------------------------------------------
    """
    spaced = ""
    placeholder = 0

    for index, char in enumerate(sentence):
        if char.isupper() and index > 0:
            spaced += sentence[placeholder:index] + " "
            placeholder = index
    spaced += sentence[placeholder:]
    spaced = spaced[0].upper() + spaced[1:].lower()
    return spaced


def string_pluralizer(string):
    """
    -------------------------------------------------------
    Pluralizes a string according to the rules:
        - if string ends with 's', 'sh', or 'ch', add 'es'
        - if string ends with 'y' but not 'ay' or 'oy', replace
            the 'y' with 'ies'
        - otherwise add 's'
    Use: pluralized = string_pluralizer(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        pluralized - a pluralized_string version of string (str)
    -------------------------------------------------------
    """
    if string.endswith("s"):
        string.replace("s", "es")
    elif string.endswith(("sh", "ch")):
        string += string[:-2] + "es"
        string += "es"
    elif string.endswith("y"):
        if string[:-2] == "ay" or string[:-2] == "oy":
            string = string
        else:
            string = string[:-1] + string[-1].replace("y", "ies")
    else:
        string += "s"
    return string


def common_suffix(str1, str2):
    """
    -------------------------------------------------------
    Returns the longest common ending of two strings.
    Use: suffix = common_suffix(str1, str2)
    -------------------------------------------------------
    Parameters:
        str1 - first string for ending comparison (str)
        str2 - second string for ending comparison (str)
    Returns:
        suffix - the longest common ending of str1 and str2 (str)
    -------------------------------------------------------
    """
    # suffix = ""
    # for index, char in enumerate(reversed(str1)):
    #     if str2[-index - 1] != char:
    #         break
    #     else:
    #         suffix += char
    # suffix = suffix[::-1]
    # return suffix
    # Fuck you for not letting me use a for loop
    suffix = ""
    index = 1
    while index <= len(str1) and index <= len(str2):
        if str1[-index] == str2[-index]:
            suffix = str1[-index] + suffix
            index += 1
        else:
            break
    return suffix


def check_isbn(isbn):
    """
    -------------------------------------------------------
    Determines if an ISBN string is valid. An ISBN string is valid if:
        - it consists of only digits and dashes ('-')
        - it contains 5 groups of digits separated by dashes
        - its first group of digits is either '978' or '979'
        - its final group of digits is a single digit
        - its entire length is 17 characters
    Use: is_valid = check_isbn(isbn)
    -------------------------------------------------------
    Parameters:
        isbn - a string (str)
    Returns:
        is_valid - True if isbn is valid, False otherwise (boolean)
    -------------------------------------------------------
    """
    is_valid = True
    parts = isbn.split('-')
    if len(isbn) != 17 or isbn.count('-') != 4 or len(parts) != 5:
        is_valid = False
    else:
        if parts[0] not in ("978", "979"):
            is_valid = False
        else:
            for part in parts[:-1]:
                if not part.isdigit():
                    is_valid = False
                    break
            if is_valid and (not parts[-1].isdigit() or len(parts[-1]) != 1):
                is_valid = False
    return is_valid


def check_word_chain(words):
    """
    -------------------------------------------------------
    Determines if a list of strings is a word chain. A word chain
    is a list of words in which the last character of a word in
    the list is the same as the first character of the next word
    in the list.
    Use: word_chain = check_word_chain(words)
    -------------------------------------------------------
    Parameters:
        words - a of strings (list of str, len > 1)
    Returns:
        word_chain - True if words is a word chain,
            False otherwise (boolean)
    -------------------------------------------------------
    """
    # word_chain = True
    # for index in range(len(words) - 1):
    #     if words[index][-1] != words[index + 1][0]:
    #         word_chain = False
    #         break
    # return word_chain
    index = 0
    word_chain = True
    while index < len(words) - 1 and word_chain:
        current_word = words[index]
        next_word = words[index + 1]
        if current_word[-1] != next_word[0]:
            word_chain = False
        index += 1
    return word_chain
