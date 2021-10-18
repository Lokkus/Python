def podstawowy_przyklad_klasy():
    class Klasa:
        count = 0;

        def __init__(self, z1, z2):
            self.z1 = z1
            self.z2 = z2

        def dispaly(self):
            self.count = 15
            print(f'Suma zmiennych:{self.z1 + self.z2}, count = {self.count}')

    k = Klasa(5, 25)
    k.dispaly()

def wspolna_zmienna_w_klasie():
    class Klasa:
        zmienna = 0
        lista = []              # wspoldzielone zmienne ktore sa mutable moga zostac zmodyfikowane na rzecz klasy a nie instancji
        def __init__(self, opis):
            self.opis = opis

        def pokaz(self):
            print(f'Jestem w klasie {self.opis}, zmienna = {self.zmienna}')
            print('elementy w liscie:')
            for i in self.lista:
                print(i, end=' ')
            print()

    # tworzymy instancje
    k1 = Klasa('Pierwsza klasa')
    k1.zmienna = 123
    k1.lista.extend([3,4,5,6,7,8])

    k2 = Klasa('Druga klasa')
    k1.pokaz()
    k2.pokaz()

def przyklad_wykorzystania_super():
    class Someone:

        def __init__(self, name, legs):
            print(f'Someone named {name} has a {legs} legs')

    class Person(Someone):
        def __init__(self, name, legs):
            super().__init__(name, legs)

    class Animal(Someone):
        def __init__(self, name, legs):
            super().__init__(name, legs)

    def testy():
        p1 = Person('Krysia', 2)
        a1 = Animal('Krowa', 4)

    testy()

def iteratory():
    s = 'abc'
    it = iter(s)
    while True:
        try:
           print(next(it))
        except StopIteration:
            print('Stop iteration')
            break

def dodanie_iteratorow_do_wlasnej_klasy():
    class Reverse:
        def __init__(self, data):
            self.data = data
            self.index = len(data)

        def __iter__(self):
            return self

        def __next__(self):
            if self.index == 0:
                raise StopIteration
            self.index = self.index-1
            return self.data[self.index]

    def test_reverse():
        rev = Reverse('cololwiek')
        iter(rev)
        for i in rev:
            print(i)

    test_reverse()


if __name__ == '__main__':
    #podstawowy_przyklad_klasy()
    #wspolna_zmienna_w_klasie()
    #przyklad_wykorzystania_super()
    #iteratory()
    dodanie_iteratorow_do_wlasnej_klasy()