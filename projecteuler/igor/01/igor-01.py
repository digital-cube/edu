'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

def i1(limit):
    s = 0
    for i in range(1, limit):
        if i%3 == 0 or i%5 == 0:
            s += i

    return s

print (i1(10))
print (i1(1000))