
''' przyklad funkcji ktora wyswietla ilosc cyfr skladajacych sie na liczbe'''


def ile_cyfr(liczba):
    print(len(str(liczba)))


def lancuchy_pierwsze_starcie():
    x = 'Ala ma kota'
    # odwracamy
    y = x[::-1]
    print(y)

    # wycinamy
    z = 'U' + x[1:]
    print(z)

    z = x[1:10:2]  # [poczatek:koniec:krok]
    print(z)

    z = x[-2::-2]
    print(x)
    print(z)

    #   A   l   a       m   a       k   o   t   a
    #  -11 -10 -9  -8  -7  -6  -5  -4  -3  -2  -1
    #   [-2::-2] wypluje tka l


def listy_pierwsze_starcie():
    L = ['jakis tekst', 123, {34: 'tu moze byc obiekt jakiejs klasy'}]
    print(L)
    L.reverse()
    print(L)
    L.append(123.55556)
    print(L)
    L2 = ['string 1', 333456]
    L.append(L2)  # tutaj dodajemy liste jako pozycje do instniejacej liczby
    print(L)
    L.pop(len(L) - 1)
    print(L)
    print(L[::-1])  # odwracamy spowrotem w celu poprawnego wyswietlenia
    # znowu usuwamy ostatni element
    L.pop(-1)
    print(L)
    L.extend(L2)
    print(L)


def listy_skladane():
    a = [b ** 2 for b in [12, 13, 15, 17]]  # podnoszenie do kwadratu
    print(a)
    a = [b ** 3 for b in [1, 2, 3, 4, 5, 6, 7, 8, 9] if b % 2 == 0]
    b = ['a', 'b', 'c', 'd']
    print(a)
    # tworzymy z tego slownik
    d = dict(zip(b, a))
    print(d)
    d = {x: y for x in a for y in b}
    print(d)

def slowniki_pierwsze_starcie():
    d = {1: 'ala ma kota', 2: 'Iza ma psa', 3: 'Ela ma chomika'}
    d[1] = 'Ala ma kota' # zmiana wartosci
    print(d)
    d[3] += ' A Kasia ma lulka'
    print(d)

    # zagniezdzenie
    d = {'dane osobowe': {'imie ': 'Marcin', 'nazwisko': 'Iksinski'}, 'zawod': ['sprzedawca', 'wozny'],
         'wiek': 40}

    print(d['dane osobowe'])
    print(d['zawod'][0])
    print(d['wiek'])

    l = list(d.keys())
    print(l)
    for a, b in d.items():
        print('klucz:', a)
        print('wartosc:', b)

    for a in sorted(d):
        print(d[a])

def krotki():
    T = (1, 2, 4, 7)
    print(len(T))
    print(T.count(2))
    print(T[0:3:2])

def pliki():
    f = open('data.txt', 'w')
    f.write('Ala ma kota\n')
    f.write('Inny tekst\n')
    f.close()
    f = open('data.txt', 'r')
    tekst = f.read()
    print(tekst)
    l = tekst.split('\n')
    print(l)

def zbiory():
    X = set("Ala ma kota")
    Y = set("Iza ma psa")
    print(X & Y)
    print(X | Y)
    X.update('Z')
    print(X)
    X.add('cokolwiek') # tutaj cokolwiek nie bedzie rozstrzelone
    print(X)
    # zbiory skladane

    Z = {x for x in [1, 2, 3, 4, 3, 1.2]}
    print(Z)

    # zbiory stosuje sie np do odfiltrowywania duplikatow:
    L = [1, 2, 4, 3, 1, 2, 7, 8, 8, 9, 0, 1, 0]
    print(L)
    # usuwamy duplikaty
    L = list(set(L))
    print(L)

    engineers = {'mateusz', 'lukasz', 'pawel'}
    managers = {'edward', 'jan', 'lukasz'}
    print(engineers & managers)
    print(engineers | managers)
    print(engineers - managers)
    print(engineers ^ managers)

def referencje():
    L1 = [1, 2, 3]
    L2 = L1 # tutaj przypisujemy jedna liste do drugiej
    L2[0] = 345
    print(L1)

    # ale
    L3 = [4,5,6]
    L4 = L3[:] # w tes sposob mozna dokonac kopii jesli nie chemy zeby referencje bylu powiazane ze spoba
    print(L3)
    print(L4)

    L4[0] = 444
    print(L3)
    print(L4)


    # is i ==

    L1 = [1,2,3]
    L2 = [1,2,3]
    print(L1 == L2) #true
    print(L1 is L2) # false

    # ale
    L3 = L1
    print(L3 is L1) # true


