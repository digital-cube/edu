




'''





'''

poziva = 0

def koren(N, delta=0.00000001):

    def metod(xp):

        global poziva
        poziva += 1

        yp = xp*xp - N

        if yp < delta:
            return xp

        k = 2*xp
        n = yp - k*xp;
        xp = -n/k

        return metod(xp)

    return metod(N)

print(koren(2), poziva)


