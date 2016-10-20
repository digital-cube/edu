'''

ovo je najjednostavnija metoda sa trazenje korena, koriscenjem izvoda mozete to uraditi u mnogo manje koraka



koren(2):

znamo da je koren(2)>0, i znamo da je koren(2)<2 => polovicemo interval izmedju 0 i 2

y=x^2 - 2

x:0       2
y:-2      2
-----------

0+2 / 2 = 1

y=1^2 - 2, = -1

------------
x:1       2
y:-1      2
----------

(1+2) / 2 = 3/2 = 1.5

1.5*1.5 - 2 = 2.25 - 2 = 0.25

x:1      1.5
y:-1     0.25
'''


poziva = 0
def koren(x, delta = 0.00000001):


    def metoda_koren(x, min, max):

        global poziva
        poziva+=1

        if max-min < delta:
            return (max+min)/2

        a = (min+max)/2
        ya = a*a - x

        if ya<=0:
            min = a
        else:
            max = a

        return metoda_koren(x , min ,max)


    return metoda_koren(x, 0, x)


print(koren(2), poziva)

1.414213564246893
1.4142135623746899
