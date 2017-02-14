

def equilibrium_v1(a):
    for p in range(1, len(a)-1):
        if sum\
                    (a[:p])==sum(a[p+1:]):
            return p
    return -1

def equilibrium(a):
    ls=None
    rs=None
    for p in range(1, len(a)-1):
        if ls == None:
            ls = sum(a[:p])
            rs = sum(a[p+1:])
            if ls == rs:
                return p
            continue

        ls+=a[p-1]
        rs-=a[p]

        if ls == rs:
            return p

    return -1

assert(equilibrium([-1, 3, -4, 5, 1, -6, 2, 1]) == 1)
assert(equilibrium([1, 2, -3, 7, 3, 1, 2, 3, 2, -2, 12, 3]) == -1)
assert(equilibrium([-7, 1, 5, 2, -4, 3, 0]) == 3)

ea=list(range(1,100))
print(ea)
s = sum(ea)
print(s)
ea.append(1111)
ea.append(s)
print(ea)

print(equilibrium(ea))