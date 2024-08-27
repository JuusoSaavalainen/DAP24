# Enter you module contents here
import math


def hypotenuse(a, b):
    """hypotenuse

    Args:
        a integer:lenght of side of right angled triangle
        b integer:lenght of side of right angled triangle

    Returns:
        float : lenght of hypotenuse
    """
    return math.sqrt(a**a + b**b)


def area(a, b):
    """area

    Args:
        a integer: lenght of triangle
        b integer: height of triagnle

    Returns:
        float : area of the right-angled triangle 
    """
    return 0.5 * a * b


__version__ = "v1"
__author__ = "Juuso"
__doc__ = "Module with functions to calculate area and hypotenuse of right-angled triangle"
