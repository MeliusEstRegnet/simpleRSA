"""
Daniel Haller

12/23/16

A first attempt at the math behind RSA.

The intent for this file is to create a library of functions to use in a main script that will import
this file.
"""

"""Python library imports."""
import math
import random
import logging

"""Adjacent file includes."""
import prime_generator


""" This line sets the logging level to DEBUG.  Default is WARNING, above DEBUG.  In order to not
print any debug statements, simply comment this line out. """
logging.basicConfig(level=logging.DEBUG)

""" We begin with two prime numbers that together will generate the public key, called p and q """

""" We will have multpile methods of generating these prime numbers, seperated into functions and
growing in complexity. """

p = prime_generator.prime1(100, 200)
q = prime_generator.prime1(200, 300)

logging.debug('p is %i', p)
logging.debug('q is %i', q)

""" Next we compute n = pq ; n makes up half of the public key """

n = p*q

logging.debug('n is %i', n)

""" n is used as the modulus for both the public and the private keys.  It is the key length. """

""" Now we compute phi(n) = phi(p)*phi(q) = (p - 1)(q - 1) = n - (p + q - 1) """

phi = n - (p + q - 1)

logging.debug('phi is %i', phi)

""" Choose an integer e such that 1 < e < phi(n) and gcd(e, phi(n)) = 1 """
def choose_e(phi):
    count = 0
    while count < 1000:
        count += 1
        prospective_e = random.randrange(2, phi)
        if gcd(prospective_e, phi) == 1:
            return prospective_e
    return -1


def gcd(a, b):
    for i in range(2, a + 1):
        if a%i==0 and b%i==0:
            return i
    else: return 1

e = choose_e(phi)

logging.debug('e is %i', e)

""" Determine d === e^-1, or d*e = 1 mod (phi(n)) solve for d """

def extended_euclidean_algorithm(e, phi):
    r_iminus1 = e
    r_i = phi
    r = 0

    s_iminus1 = 1
    s_i = 0
    s = 0

    t_iminus1 = 0
    t_i = 1
    t = 0

    while r != 1:

        q_i = math.floor(r_iminus1 / r_i)

        r = r_iminus1 - (q_i * r_i)
        s = s_iminus1 - (q_i * s_i)
        t = t_iminus1 - (q_i * t_i)

        r_iminus1 = r_i
        s_iminus1 = s_i
        t_iminus1 = t_i

        r_i = r
        s_i = s
        t_i = t

    return s

d = extended_euclidean_algorithm(e, phi)

logging.debug('d is %i', d)
logging.debug('This should equal 1 : %i', (d*e)%phi)

"""
That concludes the calculations.  Now we state the public and private keys.

p, q, phi, and d must be kept secret.  d because it is the important part of the private key, and p,
q, and phi because they can be used to calculate d
"""

public_key = (n, e)
private_key = d

"""
The encryption function for a plaintext message m is c(m) = m^e % n

For ciphertext c, the decryption function is m(c) = c^d % n
"""










