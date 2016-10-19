def f(a):

    return not a%11 and not a%12 and not a%13 and not a%14 and \
           not a%15 and not a%16 and not a%17 and not a%18 and not a%19 and not a%20

i = 2520

while True:

    if f(i):
        print(i)
        break

    i += 2520

