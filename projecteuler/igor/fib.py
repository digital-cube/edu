from common import memoize

'''
def fib(n):

    if not hasattr(fib, 'cache'):
        fib.cache = {}

    if n in fib.cache:
        return fib.cache[n]

    if n in [0, 1]:
        return 1

    fib.cache[n] = fib(n-1) + fib(n-2)
    return fib.cache[n]
'''

@memoize
def fib(n):
    return 1 if n in [0, 1] else fib(n-1) + fib(n-2)




print(fib(30))