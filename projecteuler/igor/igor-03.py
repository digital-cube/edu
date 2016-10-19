'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

import math


def is_prime(x):

    if x == 1 or x % 2 == 0:
        return False

    if x in [2, 3]:
        return True

    for i in range(3,int(math.sqrt(x))+1):
        if x % i == 0:
            return False

    return True


def next_prime(number):

    while True:
        number += 1
        if is_prime(number):
            return number


def max_factor(number):

    factors = []

    prime = 2

    while number>1:
        while number % prime == 0:
            factors.append(prime)
            number = number // prime

        prime = next_prime(prime)

    return factors[-1]


if __name__=="__main__":

    print(max_factor(600851475143))

