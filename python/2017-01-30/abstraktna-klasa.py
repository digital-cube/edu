


from abc import ABCMeta, abstractmethod

class Sloba(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, ime):
        self.ime = ime
        print("Slobo nemoj se napravis")
        pass

    @abstractmethod
    def aaa(self):
        pass

class Pera(Sloba):

    def __init__(self,ime,prezime):
        super(Pera,self).__init__(ime)
        self.prezime=prezime

        print("sloba rodio peru")

    # def aaa(self):
    #     print("daada")

S=Pera('pera','peric')

# S.aaa()