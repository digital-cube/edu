import sys

for ia in range(1, 1000):
    for ib in range(ia, 1000):
        for ic in range(ib, 1000):
            if ia+ib+ic < 1000:
                continue
            if ia**2+ib**2 == ic**2 and ia+ib+ic == 1000:
                    print(ia*ib*ic,ia,ib,ic)
                    sys.exit()
