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

if __name__=="__main__":

    i=1
    p=2
    while i<=10001:
        print (i,p)
        i+=1
        p=next_prime(p)