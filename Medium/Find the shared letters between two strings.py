"""
Find the Shared Letters between Two Strings
Given two strings, return a string containing only the letters shared between the two.

Examples
shared_letters("house", "home") ➞ "eho"

shared_letters("Micky", "mouse") ➞ "m"

shared_letters("house", "villa") ➞ ""
Notes
If none of the letters are shared, return an empty string.
The function should be case insensitive (e.g. comparing A and a should return a).
Sort the resulting string alphabetically before returning it.
"""

def Test(input, expected_result):
    return print(input ==expected_result)

def shared_letters(a, b):
    """
    :param a: first string in argument
    :param b: second string in argument
    :return: lower case string of shared characters between a & b in alphabetical order
    """
    matches = []
    a = a.lower()                # converts string a to all lower case
    b = b.lower()                # converts string a to all lower case
    for i in a:
        if i in b:
            matches.append(i)
    matches = list(set(matches)) # set() converts the list to a tuple of distinct values, list() converts back to list
    matches.sort()               # sorts list
    matches = ''.join(matches)   # converts sorted list to string
    return matches



if __name__ == '__main__':
    Test(shared_letters('house', 'home'), 'eho')
    Test(shared_letters('Micky', 'mouse'), 'm')
    Test(shared_letters('house', 'villa'), '')
    Test(shared_letters('Aa', 'aA'), 'a')
    Test(shared_letters('https://www.example.com', 'https://www.canada.ca'), './:achpstw')
    Test(shared_letters('Edabit', 'Matt'), 'at')
    Test(shared_letters('Javascript', 'Swift'), 'ist')
    Test(shared_letters('Functional programming', 'Object oriented programming'), ' acgimnoprt')