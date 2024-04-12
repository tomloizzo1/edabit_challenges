"""
Same Parity?
Create a function that takes a number as input and returns True if the sum of its digits has the same parity as the entire number. Otherwise, return False.

Examples
parity_analysis(243) ➞ True
# 243 is odd and so is 9 (2 + 4 + 3)

parity_analysis(12) ➞ False
# 12 is even but 3 is odd (1 + 2)

parity_analysis(3) ➞ True
# 3 is odd and 3 is odd and 3 is odd (3)
Notes
Parity is whether a number is even or odd. If the sum of the digits is even and the number itself is even, return True. The same goes if the number is odd and so is the sum of its digits.
Single digits will obviously have the same parities (see example #3).
"""


def Test(input, expected_result):
    return print(input == expected_result)


def parity_analysis(num):
    parity_1 = num % 2
    parity_2 = 0
    for i in list(str(num)):
        parity_2 += int(i)
    return (parity_1 == 0 and parity_2 % 2 == 0) or (parity_1 > 0 and parity_2 % 2 > 0)


if __name__ == '__main__':
    Test(parity_analysis(243), True)
    Test(parity_analysis(12), False)
    Test(parity_analysis(3), True)
    Test(parity_analysis(5), True)
    Test(parity_analysis(4), True)
    Test(parity_analysis(3453), True)
    Test(parity_analysis(0), True)
    Test(parity_analysis(123456789), True)
    Test(parity_analysis(987654321), True)
    Test(parity_analysis(13), False)
    Test(parity_analysis(182), False)
    Test(parity_analysis(133331), False)
