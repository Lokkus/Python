class MojaKlasa:
    def fun_1(self, message):
        self.message = message

# wywolywanie konstruktorow klas nadrzednych super

class Nad:
    x = []
    y = {}
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Pod(Nad):
    def __init__(self):
        print('dziala konstruktor Pod')
        super(Pod, self).__init__([5, 5, 5], {1: [6, 6, 6], 2: [7, 7, 7]})
    def pokaz(self):
        print('Z klasy Pod:')
        print(self.x)
        print(self.y)

        print('Z klasy Nad')
        print(Nad.x)
        print(Nad.y)

# klasy abstrakcyjne
from abc import ABCMeta, abstractmethod

class Super(metaclass=ABCMeta):
    @abstractmethod
    def method(self): pass

#class Sup(Super): pass # wywali blad bo nie ma zaimplementaowanej metody abstraktycyjnej
class Sup(Super):
    def method(self):
        print('metodka')



# testy
def wywolywanie_danych_z_klasy():
    x = MojaKlasa()
    x.fun_1('ala ma kota') # w ten sposob mozna nadac wartosc skladowym sklasy
    print(x.message)

def wywolywanie_konstruktorow_z_klasy_nadrzednej():
    lista_nad = [1, 2, 3]
    slownik_nad = {('x', 'y', 'z'): 'ala ma kota', ('a', 'b', 'c'): 'iza ma psa'}
    nad = Nad(lista_nad, slownik_nad)
    print(nad.x)
    print(nad.y)

    pod = Pod()
    print(pod.x)

    pod.pokaz()

def klasy_abstrakcyjne_test():
    s = Sup()
    sp = Super()

