"""
Club Entry
A night club will give you a word. For entrance, you need to provide the right number according to the provided word.

Every given word will have a doubled letter, like "dd" in addiction. To answer the right number you need to find the
doubled letter's position in the alphabet and multiply this number with 4.

Create a function that takes the argument of word and returns the right number.

Examples
club_entry("hill") ➞ 48
# 'l' is 12th in the alphabet
# 12*4 = 48

club_entry("apple") ➞ 64

club_entry("bee") ➞ 20
Notes
N/A
"""
import re
def Test(input, expected_result):
    """
    :param input: The input of a problem
    :param expected_result: The expected result of the input if properly calculated
    :return: Boolean stating if the output of the code mats the expected results
    """
    return print(input == expected_result)

def club_entry(word):
    """
    :param word: keyword with a double letter
    :return: The double letter's position in the alphabet multiplied by 4
    """
    expression = re.compile(r'(.)\1')            # Creates a search pattern finding all instance of repeating characters
    double_letter = re.findall(expression, word) # Returns a list of all non-overlapping matches
    return (ord(double_letter[0]) - 96) * 4      # Subtracts 96 from the unicode order to get position (LOWER CASE ONLY)

if __name__ == '__main__':
    Test(club_entry("lettuce"), 80)
    Test(club_entry("hill"), 48)
    Test(club_entry("apple"), 64)
    Test(club_entry("addiction"), 16)
    Test(club_entry("bee"), 20)
    Test(club_entry("zz"), 104)
    Test(club_entry("mubashirr"), 72)