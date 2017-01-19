
def f(a, b, c):

    if not hasattr(f, 'd'):
        f.d = 1

    f.d += 1
    return a+b+c+f.d


# print(f(123, 456, 789))
#
# print(f(123, 456, 789))


a = 'pera'
b = 'zika'

print (a, b)

a, b = b, a

print (a, b)

