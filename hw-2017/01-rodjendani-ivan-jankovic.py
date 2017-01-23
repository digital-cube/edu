from dates import days_between_two_dates
import sys

curent_year = int(sys.argv[1])
current_month = int(sys.argv[2])
current_day = int(sys.argv[3])

names = []
years = []
months = []
days = []

#nymd = []

lista = []
sort_lista = []

with open('input.csv', 'r') as f:

    for line in f:

        aline = line.strip().split(',')

        for c in range(1, len(aline)):
            aline[c] = int(aline[c])

        # nema potrebe da razdvajas to ui vise nizova, mozes koristiti dict, niz u nizu ili tuple
        # nymd.append( {'name':aline[0], 'year':aline[1], 'month':aline[2], 'day':aline[3]} )
        
        names.append(aline[0])
        years.append(aline[1])
        months.append(aline[2])
        days.append(aline[3])

    for c in range(0, len(names)):
        a = curent_year - years[c]

        #uradi drugacij naming (day_before nije dobro odabran naziv)
        day_before = days_between_two_dates(curent_year, current_month, current_day, curent_year,months[c],days[c])

        if day_before is False:
            day_before = days_between_two_dates(curent_year, current_month, current_day, curent_year+1, months[c],days[c])
        
        #sortirano bi nazvao red
        sortirano = (day_before, names[c], a)

        #lista za sortiranje
        sort_lista.append(sortirano)

    
    #dve petlje mozes spojiti u jednu
    lista = sorted(sort_lista)
    
    #ukoliko bas nije potrebno sacuvati original, bolje je koristi .sort metod nego sorted() funkuciju
        
    for i in range(0, len(lista)):

        # koristio si print za ispis sa odvejenim argumentima, medjutim bolje je da sve to napravis u format f-ji stringa
        # npr
        
        # print("{}) Danas {} slavi {}. rodjendan. {}".format(i+1, lista[i][1],lista[i][2],'SRECAN!!!')
        
        if lista[i][0] == 0:
            print('{}) Danas'.format(i+1), lista[i][1], 'slavi {}. rodjendan.'.format(lista[i][2]), 'SRECAN RODJENDAN !!!')
        elif lista[i][0] == 1:
            print('{}) Sutra'.format(i + 1), lista[i][1], 'slavi {}. rodjendan.'.format(lista[i][2]))

        # imas slucaj 11 dana a ne "11 dan"

        elif lista[i][0] % 10 == 1:
            print('{}) za {}'.format(i+1, lista[i][0]), 'dan', lista[i][1], 'slavi {}. rodjendan.'.format(lista[i][2]))
        else:
            print('{}) za {}'.format(i+1, lista[i][0]), 'dana', lista[i][1], 'slavi {}. rodjendan.'.format(lista[i][2]))
            

# nedostaje ti main sekcije iz koje bi pozvao program
# nedostaju ti unit testovi
