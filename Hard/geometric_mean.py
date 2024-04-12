"""
Geometric Mean
The geometric mean of numbers a and b is the square root of their product (i.e. √(ab)). For example, the geometric mean of 2 and 8 is √(2*8)=4.

Two integers (a and b) are randomly (and independently) chosen between 1 and n (inclusive) where n is an integer greater than one. Create a function that takes a number n as an argument and returns the probability that the geometric mean of a and b is an integer.

Examples
f(2) ➞ 0.5
# There are four possible pairs: (1, 1), (2, 1), (1, 2) and (2, 2).
# The pairs (1, 1) and (2, 2) are wanted (√(1*1)=1 and √(2*2)=2)
# but the pairs (2, 1) and (1, 2) are not (√(2*1)=√2 and √(1*2)=√2).
# Thus, the probability is 2/4 = 0.5.

f(10) ➞ 0.18

f(100) ➞ 0.031
Notes
Do not round your answer.
"""
import math
from itertools import product


def main(n):
    lst = options(n)
    a = cartesian(lst)
    return geometric_mean(a)


def Test(input, expected_result):
    """
    :param input: The input of a problem
    :param expected_result: The expected result of the input if properly calculated
    :return: Boolean stating if the output of the code mats the expected results
    """
    return print(input == expected_result)


def options(n):
    """
    :param n: a given number
    :return: all number from 1 to n
    """
    numbers = []
    for i in range(n):
        numbers.append(i + 1)
    return numbers


def cartesian(lst):
    """
    :param lst: a list of all numbers from 1 to n
    :return: the Cartesian Product of the list paired with itself
    """
    a = product(lst, lst)
    return (list(a))


def geometric_mean(pairs):
    """
    :param pairs: A list of tuples
    :return: The probability that a tuple selected at random is a geometric mean
    """
    denominator = len(pairs)
    geometric_count = 0
    for i in pairs:
        if math.sqrt(i[0] * i[1]) == round(math.sqrt(i[0] * i[1])):
            geometric_count += 1
    return (geometric_count / denominator)


if __name__ == '__main__':
    Test(main(2), 0.5)
    Test(main(10), 0.18)
    Test(main(100), 0.031)
