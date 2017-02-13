
a = [1, -2, 3, 30, -30, 5, -7, 2, 1, -1, 10, 12, 1, 3, 10, 15, 3, -5, 2]

#FAIL!
def m():
    s2 = sum(a)/2
    ps = 0
    for p in range(0, len(a)):
        ps += a[p]
        if ps>=s2:
            return p


def f1():
    for p in range(1, len(a)-1):
        if sum(a[:p]) == sum(a[p+1:]):
            return p


def f2():
    left_sum = a[0]
    right_sum = sum(a[2:])

    for p in range(1, len(a)-1):
        if left_sum == right_sum:
            return p

        left_sum += a[p]
        right_sum -= a[p+1]

print(m())