def initials(name):
    initial = ""
    full_name = name.split()
    for index, n in enumerate(full_name):
        if index != len(full_name) - 1:
            initial += n[0] + ". "
        else:
            initial += n[0]
    return initial


def sum_of_digits(digits):
    digit_list = []
    digits = str(digits)
    for n in digits:
        digit_list.append(int(n))
    total = sum(digit_list)
    return total


def date_printer(date):
    month = date[0:2]
    day = date[3:5]
    year = date[6:10]
    month_name = {
        "01": "January",
        "02": "February",
        "03": "March",
        "04": "April",
        "05": "May",
        "06": "June",
        "07": "July",
        "08": "August",
        "09": "September",
        "10": "October",
        "11": "November",
        "12": "December"
    }
    formatted_date = f"{month_name[month]} {day}, {year}"
    return formatted_date


def sentence_capitalize(text):
    split_text = text.split('.')
    capitalized_text = ""
    for n in split_text:
        n = n.strip()
        capitalized_sentence = n[0].upper() + n[1:] + ". "
        capitalized_text += capitalized_sentence
    return capitalized_text


def most_frequent_character(string):
    all_letters = ""
    most_char = ""
    count = 0
    for word in string:
        for char in word:
            all_letters += char
    all_letters = sorted(all_letters)
    for i in range(ord('a'), ord('z') + 1):
        letter = chr(i)
        check = all_letters.count(letter)
        if check > count:
            count = check
            most_char = letter
    sentence = f"Your most used character is '{most_char}' being used {count} times."
    return sentence


def vowel_counter(string):
    string = string.lower()
    vowels = {
        'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0
    }
    for char in string:
        if char in vowels:
            vowels[char] += 1
    total_vowels = sum(vowels.values())
    return vowels, total_vowels


def sentence_seperator(string):
    first_index = 0
    final_sentence = ""
    for second_index, char in enumerate(string):
        if char.isupper() and second_index > 0:
            final_sentence += string[first_index:second_index] + " "
            first_index = second_index
    final_sentence += string[first_index:]
    return final_sentence


def pig_latin(string):
    # this is for all yall weird mf's that speak pig latin out here
    final_sentence = ""
    split_words = string.split(" ")
    for word in split_words:
        letter = word[:1]
        final_sentence += word[1:] + letter + "ay "
    return final_sentence
