import csv
from dates import days_between_two_dates

def get_age(y1,y2):
    return y1-y2

# zamerke:
# hardkodiranje
# nedostaje ti dan/dana/danas/sutra

if __name__ == "__main__":
    with open('input.csv','r') as f:
        reader = csv.reader(f)
        lista = []
        for aline in reader:
            days = days_between_two_dates(2017, 1, 17, 2017, int(aline[2]), int(aline[3]))
            if days==False:
                days = days_between_two_dates(2017, 1, 17, 2018, int(aline[2]), int(aline[3]))
            age = get_age(int(2017),int(aline[1]))
            del aline[1:]
            aline.insert(0,days)
            aline.append(age)
            lista.append(tuple(aline))
            lista.sort()
    s = 0
    # print(lista)
    for c in lista:
        s += 1
        print('{}) {} za {} dana slavi {}. rodjendan'.format(s, c[1], c[0], c[2]))

