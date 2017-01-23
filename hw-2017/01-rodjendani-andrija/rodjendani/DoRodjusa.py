"""
PROBLEM: napisite program koji nam daje informaciju koliko dana je do cijeg rodjendana ostalo pocev od danasnjeg dana, pa u narednih godinu dana
ULAZ : danasnji datum, digitalcube-persons.csv
IZLAZ: lista do rodjendana
USLOVI: lista mora biti sortirana po blizini rodjendana
SMERNICE: ne koristimo nijednu biblioteku
datum definise GODINA-MESEC-DAN pisacemo godina, mesec, dan
moramo da vodimo racuna o tome da li je datum validan
radimo sa datumima u novoj eri.
"""

import csv

dc = []

with open('input.csv', 'r') as f:
    reader = csv.reader(f)

    for aline in reader:
        for c in range(1, len(aline)):
            aline[c] = int(aline[c])
        # print(aline)
        dc.append(aline)





def is_year_leap(y):
    """
    SOURCE: https://en.wikipedia.org/wiki/Leap_year
    """

    if y % 400 == 0:
        return True

    if y % 100 == 0:
        return False

    if y % 4 == 0:
        return True

    return False


def days_in_month(y, m):
    _days_in_month = 31 if m in [1, 3, 5, 7, 8, 10, 12] else 30

    if m == 2:
        _days_in_month = 29 if is_year_leap(y) else 28

    return _days_in_month


def is_valid_date(y, m, d):
    if d not in range(1, days_in_month(y, m) + 1):
        return False

    if m not in range(1, 12 + 1):
        return False

    return y >= 0


def is_valid_date_order(y1, m1, d1, y2, m2, d2):
    if not is_valid_date(y1, m1, d1) or not is_valid_date(y2, m2, d2):
        return False

    if y1 < y2:
        return True

    if y1 > y2:
        return False

    if m1 == m2 and d1 > d2:
        return False

    if m1 > m2:
        return False

    return True


def next_day(y, m, d):
    if d < days_in_month(y, m):
        return y, m, d + 1

    d = 1
    m += 1

    if m > 12:
        m = 1
        y += 1

    return y, m, d


def days_between_two_dates(y1, m1, d1, y2, m2, d2):
    """
    :param y1: first year ...
    :param m1:
    :param d1:
    :param y2:
    :param m2:
    :param d2:
    :return: broj dana koji dele dva datuma ili False ukolilko je ulaz nevalidan
    """

    if not is_valid_date_order(y1, m1, d1, y2, m2, d2):
        return False

    if y1 == y2 and m1 == m2:
        return d2 - d1

    nr_days = days_in_month(y1, m1) - d1
    nr_days += d2

    while True:

        m1 += 1
        if m1 > 12:
            m1 = 1
            y1 += 1

        if y1 == y2 and m1 == m2:
            break

        nr_days += days_in_month(y1, m1)

    return nr_days







yz=2017
mz=1
dz=18



def day_until_bday(y, m, d):

    if is_valid_date_order(yz,mz,dz,yz,m,d):

        return days_between_two_dates(yz,mz,dz,yz,m,d)
    else:
        if m==2 and d==29:
            x = days_between_two_dates(yz, mz, dz, yz, 12, 31)
            yp=yz+1
            while not is_year_leap(yp):
                x+=365;
                yp+=1
            return x+60

        return days_between_two_dates(yz,mz,dz,yz,12,31)+ days_between_two_dates(yz,12,31,yz+1,m,d)

def age(yz,mz,dz,y,m,d):
    if  is_valid_date_order(yz,mz,dz,yz,m,d):
        return yz-y
    else:
        return  yz-y+1


dcd = [[day_until_bday(i[1], i[2], i[3]), age(yz, mz, dz, i[1], i[2], i[3]), i[0]] for i in dc]

dcd.sort()



if __name__ == "__main__":

    #savet:
    #
    # testove odvojiti u funkcuju run_tests()
    # eventualno ih startovati ako i samo ako se program pozve u test modu.
    # 
    # bolja varijanta je napraviti poseban modul tj klasu koja nasledjuje unittest i koja ce testirati funkcionalnosti
    # modula ili klase
    
    # koristi argv za input
    #
    # savet je da se imena fajlova uvek pisu malim slovima
    #   - imena funkicja i promenljivih uvek malim slovima
    #   - imena klasa da budu camel case

    print("=================================================================================")
    print('Od danasnjeg datuma ' + str(dz)+'.'+ str(mz)+'.'+ str(yz)+'. godine imamo rodjendane po sledecem redu: ')
    print("=================================================================================")
    for i in range(0, len(dcd)):
        if (dcd[i][0]==0):
            print(str(dcd[i][2]) + " slavi " + str(dcd[i][1]) + ". rodjendan danas!")
        elif (dcd[i][0]==1):
            print(str(dcd[i][2]) + " sutra slavi " + str(dcd[i][1]) + ". rodjendan.")
        elif (dcd[i][0]%10==1 and dcd[i][0] != 11):
            print("za " + str(dcd[i][0]) + " dan " + str(dcd[i][2]) + " slavi " + str(dcd[i][1]) + ". rodjendan danas!")
        else:
            print("za " + str(dcd[i][0]) + " dana " + str(dcd[i][2]) + " slavi " + str(dcd[i][1]) + ". rodjendan.")


    assert not is_year_leap(2014)
    assert is_year_leap(2016)
    assert is_year_leap(2000)
    assert not is_year_leap(2100)

    assert days_in_month(2016, 1) == 31
    assert days_in_month(2016, 2) == 29
    assert days_in_month(2017, 2) == 28
    assert days_in_month(2100, 2) == 28
    assert days_in_month(2000, 2) == 29
    assert days_in_month(2000, 1) == 31
    assert days_in_month(2400, 2) == 29

    assert is_valid_date(2017, 1, 16)
    assert not is_valid_date(2017, 1, 32)
    assert not is_valid_date(2017, 4, 31)
    assert is_valid_date(2016, 2, 29)
    assert is_valid_date(2004, 2, 29)
    assert not is_valid_date(2100, 2, 29)
    assert not is_valid_date(2100, 2, 0)
    assert not is_valid_date(2100, 0, 10)
    assert not is_valid_date(2100, 13, 10)
    assert not is_valid_date(-22, 2, 29)

    assert not is_valid_date_order(2016, 1, 26, 2016, 1, 16)
    assert is_valid_date_order(2016, 1, 26, 2016, 2, 16)
    assert not is_valid_date_order(2016, 5, 12, 2016, 4, 16)
    assert not is_valid_date_order(2016, 5, 20, 2016, 5, 16)
    assert is_valid_date_order(2016, 2, 26, 2016, 5, 16)
    assert not is_valid_date_order(2016, 2, 126, 2016, 5, 16)
    assert not is_valid_date_order(-5, 1, 16, 2016, 1, 17)
    assert not is_valid_date_order(2015, 1, 16, -6, 1, 17)
    assert is_valid_date_order(2015, 5, 12, 2016, 4, 16)
    assert not is_valid_date_order(2018, 5, 12, 2016, 4, 16)

    assert next_day(2017, 1, 16) == (2017, 1, 17)
    assert next_day(2016, 1, 31) == (2016, 2, 1)
    assert next_day(2016, 10, 31) == (2016, 11, 1)
    assert next_day(2016, 12, 31) == (2017, 1, 1)
    assert next_day(2016, 2, 29) == (2016, 3, 1)
    assert next_day(2000, 12, 31) == (2001, 1, 1)
    assert next_day(2000, 10, 5) == (2000, 10, 6)
    assert next_day(1999, 12, 31) == (2000, 1, 1)

    assert days_between_two_dates(2017, 1, 16, 2017, 1, 17) == 1
    assert days_between_two_dates(2016, 1, 16, 2016, 1, 20) == 4
    assert days_between_two_dates(2011, 1, 16, 2016, 1, 20) == 1830
    assert days_between_two_dates(1, 1, 7, 2017, 1, 16) == 736338
    assert days_between_two_dates(1976, 8, 24, 2017, 1, 16) == 14755
    assert days_between_two_dates(1992, 12, 11, 2017, 1, 16) == 8802
    assert days_between_two_dates(1991, 4, 23, 2017, 1, 16) == 9400
    assert days_between_two_dates(1980, 8, 13, 2017, 1, 16) == 13305
    assert days_between_two_dates(1983, 11, 27, 2017, 1, 16) == 12104
    assert days_between_two_dates(1993, 3, 24, 2017, 1, 16) == 8699

    assert day_until_bday(2017,1,18) == 0
    assert day_until_bday(2000, 1, 20) == 2
    assert day_until_bday(2017, 1, 17) == 364
    assert day_until_bday(2000, 3, 1) == 42

    assert age(2017, 8, 12, 1980, 8, 13) == 37
    assert age(2017, 8, 13, 1980, 8, 13) == 37
    assert age(2017, 8, 14, 1980, 8, 13) == 38
    assert age(2017, 12, 31, 1980, 8, 13) == 38
    assert age(2000, 1, 31, 1980, 8, 13) == 20


