"""
SOURCE: https://classroom.udacity.com/courses/cs101/

PROBLEM: izracunati broj dana izmedju dva datuma

ULAZ : prvi datum, drugi datum
IZLAZ: broj dana

USLOVI: drugi datum je uvek u vremenu koje dolazi nakon prvog datuma

SMERNICE: ne koristimo nijednu biblioteku

datum definise GODINA-MESEC-DAN pisacemo godina, mesec, dan

moramo da vodimo racuna o tome da li je datum validan

radimo sa datumima u novoj eri.
"""


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

    if m not in range(1, 12+1):
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
        return y, m, d+1

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

    # while (y1, m1, d1) != (y2, m2, d2):
    #
    #     y1, m1, d1 = next_day(y1, m1, d1)
    #     nr_days += 1

    while True:

        m1 += 1
        if m1 > 12:
            m1 = 1
            y1 += 1

        if y1 == y2 and m1 == m2:
            break

        nr_days += days_in_month(y1, m1)

    return nr_days


if __name__ == "__main__":

    cy, cm, cd = 2017, 1, 18
    ty, tm, td = 1976, 1, 1
    tcy, tcm, tcd = cy, tm, td

    if is_valid_date_order(cy, cm, cd, tcy, tcm, tcd):
        days_to_persons_birthday = days_between_two_dates(cy, cm, cd, tcy, tcm, tcd)
        will_celbrate_birthday_nr = cy - ty
    else:
        days_to_persons_birthday = days_between_two_dates(cy, cm, cd, tcy + 1, tcm, tcd)
        will_celbrate_birthday_nr = cy - ty + 1

    print('dana do {} rodjendana ove osobe ima: {}'.format(will_celbrate_birthday_nr, days_to_persons_birthday))

    # print ( days_between_two_dates(ty, tm, td, cy, cm, cd) )

    # assert not is_year_leap(2014)
    # assert is_year_leap(2016)
    # assert is_year_leap(2000)
    # assert not is_year_leap(2100)
    #
    # assert days_in_month(2016, 1) == 31
    # assert days_in_month(2016, 2) == 29
    # assert days_in_month(2017, 2) == 28
    # assert days_in_month(2100, 2) == 28
    # assert days_in_month(2000, 2) == 29
    # assert days_in_month(2400, 2) == 29
    #
    # assert is_valid_date(2017, 1, 16)
    # assert not is_valid_date(2017, 1, 32)
    # assert not is_valid_date(2017, 4, 31)
    # assert is_valid_date(2016, 2, 29)
    # assert is_valid_date(2004, 2, 29)
    # assert not is_valid_date(2100, 2, 29)
    # assert not is_valid_date(2100, 2, 0)
    # assert not is_valid_date(2100, 0, 10)
    # assert not is_valid_date(2100, 13, 10)
    # assert not is_valid_date(-22, 2, 29)
    #
    # assert not is_valid_date_order(2016, 1, 26, 2016, 1, 16)
    # assert is_valid_date_order(2016, 1, 26, 2016, 2, 16)
    # assert not is_valid_date_order(2016, 5, 12, 2016, 4, 16)
    # assert not is_valid_date_order(2016, 5, 20, 2016, 5, 16)
    # assert is_valid_date_order(2016, 2, 26, 2016, 5, 16)
    # assert not is_valid_date_order(2016, 2, 126, 2016, 5, 16)
    # assert not is_valid_date_order(-5, 1, 16, 2016, 1, 17)
    # assert not is_valid_date_order(2015, 1, 16, -6, 1, 17)
    # assert is_valid_date_order(2015, 5, 12, 2016, 4, 16)
    # assert not is_valid_date_order(2018, 5, 12, 2016, 4, 16)
    #
    # assert next_day(2017, 1, 16) == (2017, 1, 17)
    # assert next_day(2016, 1, 31) == (2016, 2, 1)
    # assert next_day(2016, 10, 31) == (2016, 11, 1)
    # assert next_day(2016, 12, 31) == (2017, 1, 1)
    # assert next_day(2016, 2, 29) == (2016, 3, 1)
    # assert next_day(2000, 12, 31) == (2001, 1, 1)
    # assert next_day(2000, 10, 5) == (2000, 10, 6)
    # assert next_day(1999, 12, 31) == (2000, 1, 1)
    #
    # assert days_between_two_dates(2017, 1, 16, 2017, 1, 17) == 1
    # assert days_between_two_dates(2016, 1, 16, 2016, 1, 20) == 4
    # assert days_between_two_dates(2011, 1, 16, 2016, 1, 20) == 1830
    # assert days_between_two_dates(2011, 1, 16, 2016, 1, 20) == 1830
    # assert days_between_two_dates(1, 1, 7, 2017, 1, 16) == 736338
    # assert days_between_two_dates(1976, 8, 24, 2017, 1, 16) == 14755
    # assert days_between_two_dates(1992, 12, 11, 2017, 1, 16) == 8802
    # assert days_between_two_dates(1991, 4, 23, 2017, 1, 16) == 9400
    # assert days_between_two_dates(1980, 8, 13, 2017, 1, 16) == 13305
    # assert days_between_two_dates(1983, 11, 27, 2017, 1, 16) == 12104
    # assert days_between_two_dates(1993, 3, 24, 2017, 1, 16) == 8699
    #

