import datetime
import sys

nowYear = datetime.datetime.now().year

zbir_godina = 0
broj_osoba = 0

with open('input.txt') as file:
    for row in file:
        row = row.replace('\n', ' ')
        arow = row.split(' ')[:3]
        if len(arow) < 3:
            print('neispravan ulazni format')
            sys.exit(1)

        try:
            arow[2] = int(arow[2])

            if arow[2] < 1900 or arow[2] > nowYear:
                print('godiste za osobu {} je izvan dozvoljenog ranga'.format(row))
                sys.exit(3)

            zbir_godina += nowYear - arow[2]
            broj_osoba += 1

        except Exception as e:
            print('godiste nije u odgovarajucem formatu')
            sys.exit(2)

        print(arow)

prosek = round(float(zbir_godina) / broj_osoba, 2)

print('prosek godina je: {}'.format(prosek))

sys.exit(0)