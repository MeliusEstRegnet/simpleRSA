"""
Daniel Haller

12/23/16

A first attempt at the math behind RSA.

The intent for this file is to create a library of functions to use in a main script that will import
this file.
"""

import math
import random
import logging

""" This line sets the logging level to DEBUG.  Default is WARNING, above DEBUG.  In order to not
print any debug statements, simply comment this line out. """
logging.basicConfig(level=logging.DEBUG)

""" We begin with two prime numbers that together will generate the public key, called p and q """

""" We will have multpile methods of generating these prime numbers, seperated into functions and
growing in complexity. """


"""Returns a random prime number between 2 and x. Basic method."""
def prime1(x):
    a = random.randrange(2, x)
    logging.debug('a is %i', a)
    for i in range(2, math.floor(math.sqrt(x))):
        if a % i == 0:
            """Not prime."""
            return -1
    else:
        return 1

logging.debug(prime1(100))


p = 61
q = 53

""" Next we compute n = pq ; n makes up half of the public key """

n = p*q

logging.debug(n)

""" n is used as the modulus for both the public and the private keys.  It is the key length. """

""" Now we compute phi(n) = phi(p)*phi(q) = (p - 1)(q - 1) = n - (p + q - 1) """

phi = n - (p + q - 1)

logging.debug(phi)

""" Choose an integer e such that 1 < e < phi(n) and gcd(e, phi(n)) = 1 """

e = 17

""" Determine d === e^-1, or d*e = 1 mod (phi(n)) solve for d """

d = 2753

logging.debug('This should equal 1 : %i', (d*e)%phi)
