"""
Return the Sum of the Two Smallest Numbers
Create a function that takes a list of numbers and returns the sum of the two lowest positive numbers.

Examples
sum_two_smallest_nums([19, 5, 42, 2, 77]) ➞ 7

sum_two_smallest_nums([10, 343445353, 3453445, 3453545353453]) ➞ 3453455

sum_two_smallest_nums([2, 9, 6, -1]) ➞ 8

sum_two_smallest_nums([879, 953, 694, -847, 342, 221, -91, -723, 791, -587]) ➞ 563

sum_two_smallest_nums([3683, 2902, 3951, -475, 1617, -2385]) ➞ 4519
Notes
Don't count negative numbers.
Floats and empty lists will not be used in any of the test cases.
"""


def sum_two_smallest_nums(lst):
    positive_list = []
    for i in lst:
        if i > 0:
            positive_list.append(i)
    positive_list.sort()
    return positive_list[0] + positive_list[1]

if __name__ == '__main__':
    test1 = [19, 5, 42, 2, 77]
    test2 = [10, 343445353, 3453445, 3453545353453]
    test3 = [2, 9, 6, -1]
    test4 = [879, 953, 694, -847, 342, 221, -91, -723, 791, -587]
    test5 = [3683, 2902, 3951, -475, 1617, -2385]
    print(sum_two_smallest_nums(test1) == 7 )
    print(sum_two_smallest_nums(test2) == 3453455)
    print(sum_two_smallest_nums(test3) == 8)
    print(sum_two_smallest_nums(test4) == 563)
    print(sum_two_smallest_nums(test5) == 4519)