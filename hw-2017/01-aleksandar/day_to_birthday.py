#komituj sve sto ti je neohodno da pokrenes projekat na drugom racunaru

#savet: pogledaj kako sam kod ivana napravio obradu argumenata

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
    while True:
        m1 += 1
        if m1 > 12:
            m1 = 1
            y1 += 1
        if y1 == y2 and m1 == m2:
            break
        nr_days += days_in_month(y1, m1)
    return nr_days


def days_to_birthday(birthday_y, birthday_m, birthday_d, today_y, today_m, today_d):
    if is_valid_date_order(today_y, today_m, today_d, today_y, birthday_m, birthday_d):
        return  days_between_two_dates(today_y, today_m, today_d, today_y, birthday_m,
                                       birthday_d)
    else:
        return  days_between_two_dates(today_y, today_m, today_d, today_y + 1,
                                       birthday_m, birthday_d)


def how_many_years_has(birthday_y, birthday_m, birthday_d, today_y, today_m, today_d):
    if is_valid_date_order(today_y, today_m, today_d, today_y, birthday_m, birthday_d):
        return today_y - birthday_y
    else:
        return today_y - birthday_y + 1


def grammar_of_day(day):
    
    if day == 0:
        return 'Danas'
    if day == 1:
        return 'Sutra'
    if day == 2:
        return 'Prekosutra'
    if day == 11:
        return 'Za 11 dana'

    day = str(day)
    if day[-1]=='1':
        return 'Za {} dan'.format(day)
    
    return 'Za {} dana'.format(day)
    
      
    '''
    
    #izoluj samo ono sto je promenljivo, nemoj da ponavljas stvari
    
    day = str(day)
    if day == '1':
        return "Sutra"
    if day == '2':
        return "Prekosutra"
    if day[-1] in ['3','4','5','6','7','8','9']:
        return "Za {} dana".format(day)
    if day[-2:] in ['21','31','41','51','61','71','81','91']:
        return "Za {} dan".format(day)
    if day[-2:] in ['10','11','20','30','40','50','60','70','80','90','00']:
        return "Za {} dana".format(day)
    if day == '0':
        return "Danas"
    '''

def sorting(dani):
    dani.sort()
    for i in dani:
        print(i[1])


if __name__ == "__main__":

    # zamerke:
    #  mesanje programa - mogao si kao sto su to ivan i mladen uradili, da importujes modul ili funkciju iz modula koji smo napravili 

    year = 2017
    month = 1
    day = 22
    birthday = []
    with open('input.csv', 'r') as f:
        for line in f:
            aline = line.strip().split(',')
            for c in range(1, len(aline)):
                aline[c] = int(aline[c])
            h_m_d=days_to_birthday(aline[1], aline[2], aline[3], year, month, day)
            birthday.append((h_m_d, "{} {} slavi {}. rodjendan!".format(grammar_of_day(h_m_d), aline[0], \
            how_many_years_has(aline[1], aline[2], aline[3], year, month, day))))

    # nema potrebe da odvajs to u funkciju koja radi trivijalnu stvar
    sorting(birthday)
    
    # ako se funkcija zove sorting, ne treba da ima side_efect, tj print unutar funkcije

    # Unit tests
    assert grammar_of_day(1) == "Sutra"
    assert not grammar_of_day(1) == "sutra"
    assert not grammar_of_day(0) == "Sutra"
    assert grammar_of_day(3) == "Za 3 dana"
    assert grammar_of_day(5) == "Za 5 dana"
    assert grammar_of_day(2) == "Prekosutra"
    assert not grammar_of_day(2) == "prekosutra"
    assert not grammar_of_day(2) == "za 2 dana"
    assert grammar_of_day(21) == "Za 21 dan"
    assert grammar_of_day(41) == "Za 41 dan"
    assert grammar_of_day(71) == "Za 71 dan"
    assert not grammar_of_day(66) == "Za 66 dan"
    assert grammar_of_day(10) == "Za 10 dana"
    assert grammar_of_day(90) == "Za 90 dana"
    assert grammar_of_day(100) == "Za 100 dana"
    assert grammar_of_day(200) == "Za 200 dana"
    assert grammar_of_day(361) == "Za 361 dan"

    #primedba: obavezno napisi unittest za spec. slucaj (11)
    assert grammar_of_day(11) == "Za 11 dana"


    assert how_many_years_has(1991,1,23,2017,1,22) == 26
    assert not how_many_years_has(1991, 1, 20, 2017, 1, 22) == 26
    assert how_many_years_has(1991, 1, 20, 2017, 1, 22) == 27
    assert not how_many_years_has(1933, 1, 20, 2017, 1, 22) == 86
    assert how_many_years_has(1986, 1, 23, 2017, 1, 23) == 31
    assert not how_many_years_has(1986, 1, 23, 2017, 1, 24) == 31
