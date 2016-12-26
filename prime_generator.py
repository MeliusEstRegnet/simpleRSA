
"""
Contains functions to generate prime numbers.
Included in math_RSA.py

Author: Daniel Haller
Date: 12/26/2016
"""

import math
import logging
import random

logging.basicConfig(level=logging.DEBUG)

"""Returns a random prime number between x and y. Basic method.
Note that if there is no prime between x and y, """
def prime1(x, y):
    count = 0
    while count < 1000:
        count+= 1
        a = random.randrange(x, y)
        """logging.debug('a is %i', a)"""
        for i in range(2, math.floor(math.sqrt(x))):
            if a % i == 0:
                """Not prime."""
                break
        else:
            return a


