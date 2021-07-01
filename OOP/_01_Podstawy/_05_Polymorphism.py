class A:
    _napis1 = ''
    _napis2 = ''
    def __init__(self, n1, n2):
        self._napis1 = n1
        self._napis2 = n2

    def pokaz(self):
        print(self._napis1)
        print(self._napis2)

class B(A):
    def pokaz(self):
        print(self._napis1)
        print(self._napis2)
        print('KLASA B')

class C(A):
    def pokaz(self):
        print(self._napis1)
        print(self._napis2)
        print('Klasa C')

if __name__ == '__main__':
    lista_obiektow = [A('napis1', 'napis2'), B('napis3', 'napis4'), C('napis5', 'napis6')]
    for func in lista_obiektow:
        func.pokaz()