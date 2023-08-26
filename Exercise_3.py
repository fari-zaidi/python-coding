
#########################################################################################
#                                    Exercise 3 (A)
#########################################################################################

def is_str_palindrome(s: str) -> bool:
    """
    Determines whether or not the input string is a palindrome.
    If a string reads the same forward as it does backward, it is referred to as a palindrome..

    :parameter s: input string to be checked
    :return: True if "s" is a palindrome, else False
    """
    # Lowercase the string and eliminate any spaces or other special characters.
    s = ''.join(filter(str.isalnum, s.lower()))
    # Compare the reversed string with the original string
    return s == s[::-1]


#########################################################################################
#                                    Exercise 3 (B)
#########################################################################################

def up_most_frequent_letter(s: str) -> str:
    """
    returns the input string's most frequent letter or digit..
    Characters that are neither letters nor digits are ignored.
    """
    # Convert string to uppercase
    s = s.upper()
    # Get rid of all characters that aren't letters or numbers.
    s = ''.join(filter(str.isalnum, s))
    # Making a dictionary to keep track of the frequency of each letter or number.
    frq_dct = {}
    for char in s:

        if char in frq_dct:
            # increase the frequency if char occurs more than once
            frq_dct[char] += 1
        else:
            frq_dct[char] = 1

    # Find the letter or numeral that appears the most frequently.
    most_frqt = max(frq_dct, key=frq_dct.get)
    return most_frqt


#########################################################################################
#                                    Exercise 3 (C)
#########################################################################################


def count_char(s: str) -> dict:
    """
    Returns a dictionary after counting the number of letters, spaces, and digits in the provided string.
    """
    count_let = 0
    count_sp = 0
    count_dig = 0
    # Count the number of letters, spaces, and digits in the string
    for ch in s:
        if ch.isalpha():
            count_let += 1
        elif ch.isspace():
            count_sp += 1
        elif ch.isdigit():
            count_dig += 1
    # Create a dictionary with the counts
    output_counts = {'letters': count_let, 'spaces': count_sp, 'digits': count_dig}
    return output_counts


#########################################################################################
#                                Auxiliary functions:
#########################################################################################
"""
1) isalnum() :- method of 'str' class return 'TRUE' if alphanumeric(only digits and and letters) string occurs and 'FALSE' otherwise.
used to clean the string in function is_str_palindrome() and up_most_frequent_letter()

2) isalpha() :- method returns 'TRUE' if only alphabetic chars are in string only letters
used in function count_char()

3) isspace() :- method return 'TRUE' if only whitespaces occurs and otherwise 'FALSE'
used in function count_char()

4) isdigit() :- method returns 'TRUE' if string only consist of digits, used in function count_char()

5) max() :- returns the key in a dictionary that has the highest value..

6) get() :- extract value of key in dictionary. Returns 0 if key not present

"""

