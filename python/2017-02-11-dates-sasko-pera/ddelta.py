class InvalidDataType(BaseException):
    pass

def is_leap_year(year):

    if year % 400 == 0:
        return True

    if year % 100 == 0:
        return False

    return year % 4 == 0

def days_in_month(year, month):

    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31

    if month == 2:
        return 29 if is_leap_year(year) else 28

    return 30


def is_date_valid(date):

    if not isinstance(date, tuple):
        return False

    if len(date) != 3:
        return False

    for i in (0, 1, 2):
        if not isinstance(date[i], int):
            return False

    if date[1] <= 0 or date[1] > 12:
        return False

    if date[2] <= 0 or date[2] > days_in_month(date[0], date[1]):
        return False

    return True

def next_date(date):

    if not is_date_valid(date):
        raise InvalidDataType

    year, month, day = date

    day += 1
    if day > days_in_month(year, month):
        day = 1
        month += 1

        if month > 12:
            month = 1
            year += 1

    return year, month, day


def ddelta(date1, date2):

    if not (is_date_valid(date1) and is_date_valid(date2)):
        raise InvalidDataType

    if date1 == date2:
        return 0

    swapped = False

    if date1 > date2:
        swapped = True
        date1, date2 = date2, date1


    if date1[:2] == date2[:2]:
        return date2[2]-date1[2] if not swapped else date1[2]-date2[2]

    # nr_days = 0
    # while date1 != date2:
    #     date1 = next_date(date1)
    #     nr_days += 1
    #

    nr_days = ddelta(date1, (date1[0], date1[1], days_in_month(date1[0], date1[1])))

    year, month = date1[0], date1[1]

    while True:

        month += 1
        if month > 12:
            year += 1
            month = 1

        if (year, month) == (date2[0], date2[1]):
            break

        nr_days += days_in_month(year, month)

    nr_days += date2[2]


    return nr_days if not swapped else -nr_days
