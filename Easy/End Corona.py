"""End Corona!
Create a function that takes the number of daily average recovered cases recovers, daily average new_cases, current active_cases, and returns the number of days it will take to reach zero cases.

Examples
end_corona(4000, 2000, 77000) ➞ 39

end_corona(3000, 2000, 50699) ➞ 51

end_corona(30000, 25000, 390205) ➞ 79
Notes
The number of people who recover per day recovers will always be greater than daily new_cases.
Be conservative and round up the number of days needed."""

def Test(input, expected_result):
    return print(input ==expected_result)

def end_corona(recovers, new_cases, active_cases):
    days = 0
    while active_cases > 0:
        active_cases = active_cases - (recovers - new_cases)
        days += 1
    return days

if __name__ == '__main__':
    import unittest
    Test(end_corona(4000, 2000, 77000), 39)
    Test(end_corona(3000, 2000, 50699), 51)
    Test(end_corona(30000, 25000, 390205), 79)
    Test(end_corona(260000, 255000, 20511691), 4103)