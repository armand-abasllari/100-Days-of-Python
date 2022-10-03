"""
    This function takes the height and width of a wall, and the coverage of a can of paint, and returns
    the number of cans of paint needed to cover the wall.
    
    :param height: test_h
    :param width: width of the wall
    :param cover: the amount of square feet that one can of paint covers
"""
import math


def paint_calc(height,width,cover):

    x = test_h * test_w
    y = math.ceil(x / coverage)
    print(f"You'll need {y} cans of paint.")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
