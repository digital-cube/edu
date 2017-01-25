import datetime

class Izuzetak(NameError):
    pass


class Person(object):

    def __init__(self, ime, prezime):
        self.ime = ime
        self.prezime = prezime
        self.datum_rodjenja = None

    def set_datum_rodjenja(self, datum_rodjenja):
        self.datum_rodjenja = datum_rodjenja

    def __str__(self):
        return "moje ime je {} {} i rodjen sam {}, a rodjendan ce mi biti za {} dan(a)".format(self.ime, self.prezime, self.datum_rodjenja.strftime("%d %B %Y"),self.dana_do_rodjendana())

    def dana_do_rodjendana(self):
        if not self.datum_rodjenja:
            return None

        cd = datetime.datetime.now()

        rodjendan = datetime.datetime(cd.year, self.datum_rodjenja.month, self.datum_rodjenja.day)

        if rodjendan>cd:
            return (rodjendan-cd).days

        return (cd-rodjendan).days


class Muskarac(Person):
    def __init__(self, ime, prezime):
        super(Muskarac, self).__init__(ime, prezime)


class Devojka(Person):
    def __init__(self, ime, prezime):
        super(Devojka, self).__init__(ime, prezime)

    def __str__(self):
        return "moje ime je {} {} i rodjena sam {}, a rodjendan ce mi biti za {} dan(a)".format(self.ime, self.prezime, self.datum_rodjenja.strftime("%d %B %Y"),self.dana_do_rodjendana())


if __name__=="__main__":

    mladen = Muskarac('mladen', 'milicevic')
    munira = Devojka('munira', 'hasanagic')

    mladen.set_datum_rodjenja(datetime.datetime(1993, 3, 24))
    munira.set_datum_rodjenja(datetime.datetime(1992, 12, 11))

    print(mladen)
    print(munira)

    print(mladen.dana_do_rodjendana())