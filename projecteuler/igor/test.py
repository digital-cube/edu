import sys

def koren_2(x, delta = 0.00000001):


    delta = 0.1 * delta;


    def metoda_koren(x, min, max):

        if max-min < delta:
            return (max+min)/2

        a = (min+max)/2
        ya = a*a - x

        if ya<=0:
            min = a
        else:
            max = a

        return metoda_koren(x , min ,max)

    if x < 0:
        raise NameError('can not calculate root of negative number')
    if x in [0,1]:
        return x
    elif x > 1:
        return metoda_koren(x, 0, x)
    else:
        return metoda_koren(x, x, 1)


# ne radi za brojeve 0 - 1

def koren_n(N , delta=0.00000001):

    def metod(xp):

        yp = xp*xp - N

        if yp < delta:
            return xp

        k = 2*xp
        n = yp - k*xp;
        xp = -n/k

        return metod(xp)

    return metod(N)


def koren(x, delta):


    return 0


def stop_testing(name):
    print("test {} FAILED".format(name))
    sys.exit()


def info(name, message):
    print("test {} {}".format(name, message))


def test_sqrt_2():
    if abs(round(koren(2, 0.001), 3) - 1.414) >= 0.001:
        stop_testing('test_sqrt_2')

    info('test_sqrt_2', 'PASSED')


def test_sqrt_3():
    if abs(round(koren(3, 0.001), 3) - 1.732) >= 0.001:
        stop_testing('test_sqrt_3')

    info('test_sqrt_3', 'PASSED')


def test_sqrt_4():
    if abs(round(koren(4, 0.001), 3) - 2) >= 0.001:
        stop_testing('test_sqrt_4')

    info('test_sqrt_4', 'PASSED')


def test_sqrt_0():

    if abs(round(koren(0, 0.001), 3) - 0) >= 0.001:
        stop_testing('test_sqrt_0')

    info('test_sqrt_0', 'PASSED')


def test_sqrt_1():

    if abs(round(koren(1, 0.001), 3) - 1) >= 0.001:
        stop_testing('test_sqrt_1')

    info('test_sqrt_1', 'PASSED')


def test_sqrt_0_5():

    if abs(round(koren(0.5, 0.001), 3) - 0.707) >= 0.001:
        stop_testing('test_sqrt_0_5')

    info('test_sqrt_0_5', 'PASSED')

def test_sqrt_big_number():

    if abs(round(koren(999999993, 0.001), 3) - 31622.776) >= 0.001:
        stop_testing('test_sqrt_big_number')

    info('test_sqrt_big_number', 'PASSED')

def test_sqrt_minus_1():

    try:
        koren(-1, 0.001)
        stop_testing('test_sqrt_minus_1')

    except NameError as e:
        info('test_sqrt_minus_1', 'PASSED')


if __name__=="__main__":

    test_sqrt_2()
    test_sqrt_3()
    test_sqrt_4()
    test_sqrt_0()
    test_sqrt_1()
    test_sqrt_0_5()
    test_sqrt_minus_1()
    test_sqrt_big_number()

