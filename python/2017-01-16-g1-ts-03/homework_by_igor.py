
from dates import is_valid_date_order, days_between_two_dates

import csv


def srb_dan_or_dana(n):
    ns = str(n)

    if len(ns) == 1:
        return "dan" if ns == '1' else "dana"

    if len(ns) > 1:
        return "dan" if (ns[-1] == '1' and ns[-2] != '1') else "dana"

    raise NameError("Invalid data")


def load_data(filename):

    try:

        persons = []

        with open(filename, 'r') as f:
            reader = csv.reader(f)
            for aline in reader:
                for c in range(1, len(aline)):
                    aline[c] = int(aline[c])

                persons.append([None, aline[0], (aline[1], aline[2], aline[3])])

        return persons

    except Exception as e:

        return False


def create_sorted_list_of_incoming_birthdays(cdy, cdm, cdd, persons):

    for person in persons:

        target_year = (cdy + 1) if not is_valid_date_order(cdy, cdm, cdd, cdy, person[2][1], person[2][2]) else cdy
        days_till_next_birthday = days_between_two_dates(cdy, cdm, cdd, target_year, person[2][1], person[2][2])
        which_birthday = target_year - person[2][0];
        person[0] = (days_till_next_birthday, which_birthday)

    persons.sort()

    return persons

if __name__=="__main__":

    assert srb_dan_or_dana(1) == 'dan'
    assert srb_dan_or_dana(2) == 'dana'
    assert srb_dan_or_dana(7) == 'dana'
    assert srb_dan_or_dana(0) == 'dana'
    assert srb_dan_or_dana(21) == 'dan'
    assert srb_dan_or_dana(31) == 'dan'
    assert srb_dan_or_dana(11) == 'dana'
    assert srb_dan_or_dana(5511) == 'dana'

    p = [[None, 'Igor Jeremic', (1976, 1, 1)]]
    create_sorted_list_of_incoming_birthdays(2017, 1, 17, p)
    assert p[0][0] == (349, 42)

    p = [[None, 'Igor Jeremic', (1976, 1, 1)], [None, 'Slobodan Dolinic', (1980, 2, 1)]]
    create_sorted_list_of_incoming_birthdays(2017, 1, 17, p)
    assert p[0][0] == (15, 37)
    assert p[1][0] == (349, 42)

    persons = load_data('input.csv')

    print(persons)

    if persons:
        create_sorted_list_of_incoming_birthdays(2017, 1, 17, persons)

    for p in persons:
        br_dana = p[0][0]
        do_rodjendana = p[0][1]

        print('jos {} {} do {} rodjendana za korisnika {}'.format(br_dana, srb_dan_or_dana(br_dana), do_rodjendana, p[1]))

