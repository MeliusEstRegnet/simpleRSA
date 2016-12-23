"""
Daniel Haller

12/23/16

A first attempt at the math behind RSA.
"""

import math
import logging

""" This line sets the logging level to DEBUG.  Default is WARNING, above DEBUG.  In order to not
print any debug statements, simply comment this line out. """
logging.basicConfig(level=logging.DEBUG)

""" We begin with two prime numbers that together will generate the public key, called p and q """

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
