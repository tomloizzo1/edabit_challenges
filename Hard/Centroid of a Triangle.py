"""
Centroid of a Triangle
If you have a triangular shape cut from a piece of cardboard, the centroid of the triangle would be the spot where it balances on the point of a pencil. The location of the centroid is easy to calculate if you know the x, y coordinates of the vertices:

The x coordinate of the centroid is at (x1 + x2 + x3) / 3
The y coordinate of the centroid is at (y1 + y2 + y3) / 3
x1, y1, x2, y2, x3, y3 are the coordinates of the three vertices.

Create a function that calculates the position of the centroid given the coordinates of the vertices. Round the answers to two decimal places. If the three points given do not form a triangle, return False.

Examples
centroid(0, 0, 3, 0, 3, 3) ➞ (2.0, 1.0)

centroid(2, 2, 8, -2, 0, -3) ➞ (3.33, -1.0)

centroid(1, 1, 2, 2, 3, 3) ➞ False
Notes
The arguments are given in the order shown above: x1, y1, x2, y2, x3, y3.
If the three points do not form a triangle, they must lie in a straight line.
"""



def Test(input, expected_result):
    return print(input ==expected_result)


def centroid(x1, y1, x2, y2, x3, y3):
    a = x2-x1
    b = x3-x2
    if x2-x1 == 0:
        a = 00000000000.1
    if x3-x2 == 0:
        b = 00000000000.1

    x = round( (x1 + x2 + x3) / 3, 2)
    y = round( (y1 + y2 + y3) / 3, 2)
    if round((y2-y1)/a,2) == round((y3-y2)/b,2):
        return False
    else:
        return(x,y)

if __name__ == '__main__':
    Test(centroid(0, 0, 3, 0, 3, 3), (2.0, 1.0))
    Test(centroid(5, 3, -3, -2, -1, 4), (0.33, 1.67))
    Test(centroid(2, 2, 8, -2, 0, -3), (3.33, -1.0))
    Test(centroid(5, 3, 5, -1, -4, 1), (2.0, 1.0))
    Test(centroid(-1, -3, 1, 3, 2, 6), False)
    Test(centroid(3, 0, 0, 3, 6, 3), (3.0, 2.0))