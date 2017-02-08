parts = 5
import hashlib


def cshash_sum_md5(s):
    return hashlib.md5(s.encode()).hexdigest()[:3]

def cshash_sum_of_letters_with_prime_numbers_position(s):

    primes = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
    res = 0
    for i in range(len(s)):
        res += (primes[i])*ord(s[i])

    return res % parts


def cshash_sum_of_letters_with_position(s):

    res = 0
    for i in range(len(s)):
        res += (i+1)*ord(s[i])

    return res % parts


def cshash_sum_of_letters(s):

    return sum([ ord(c) for c in s ]) % parts

def cshash_length(s):

    return len(s)

if __name__=="__main__":


    from binarna_pretraga import db_index

    raspodela={}

    indeksirano = {}

    for i in db_index:
        # rasporedjen_u = cshash_sum_md5(i[0])
        # rasporedjen_u = cshash_sum_of_letters_with_prime_numbers_position(i[0])
        rasporedjen_u = cshash_sum_of_letters_with_position(i[0])
        # rasporedjen_u = cshash_sum_of_letters(i[0])
        # rasporedjen_u = cshash_length(i[0])
        if rasporedjen_u not in raspodela:
            raspodela[rasporedjen_u] = 0

        raspodela[rasporedjen_u] += 1

        if rasporedjen_u not in indeksirano:
            indeksirano[rasporedjen_u] = []

        indeksirano[rasporedjen_u].append(i)

        print("{:20} {}".format(i[0],rasporedjen_u))

    print(raspodela)
    for i in raspodela:
        print(i, indeksirano[i] if i in indeksirano else [] )