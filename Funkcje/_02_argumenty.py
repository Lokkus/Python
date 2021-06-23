def argumenty_modyfikowalne(a, b):
    a += 10
    b[0] = 'Jakis sobie test'

def argumenty_modyfikowalne_test():
    a = 123
    b = [1,2,3]
    print('Przed modyfikacja:')
    print(a)
    print(b)
    argumenty_modyfikowalne(a, b)
    print('Po modyfikacji')
    print(a)
    print(b)

    print("Unikanie modyfikacji")
    b = [1,2,3]
    argumenty_modyfikowalne(a, b[:]) # tutaj przekazujemy argument jako kopie
    print('Po modyfikacji')
    print(a)
    print(b)

def zwracanie_kilku_argumentow():
    a = 123
    b = [i for i in range(1, 100, 2) if all([i % 3 == 1 and i % 6 == 1])]
    c = 'Ala ma kota'
    return a, b, c # to bedzie zwrocone jako krotka

def zwracanie_kilku_argumentow_test():
    x = zwracanie_kilku_argumentow()
    print(x)
    x = list(x) # konwersja na liste - nie mozna modyfikowac krotek
    x[0] = 'wwwwww'
    print(x)
    # mozna tez zrobic tak
    a, b, c = zwracanie_kilku_argumentow() # to jest rozbicie na kilka parametrow, kazde z nich nie jest juz krotka
    print(a)
    print(b)
    print(c)

def slowa_kluczowe(a = 1, b = 2, c = 3):
    print(a)
    print(b)
    print(c)

def slowa_kluczowe_2(x, y, z=10): # tu nie moze być sytuacji ze jest np (x, y=1, z) w parametrach funkcji, domyslne musza byc max od prawej do lewej
    print(x, y, z)



def slowa_kluczowe_test():
    slowa_kluczowe()
    slowa_kluczowe(c=123, b=10)
    slowa_kluczowe(b=55)
    slowa_kluczowe_2(1,2,3)


def dowolna_liczba_argumentow(*args):
    print(args) # to jest zamieniane w krotke

def dowolna_liczba_argumentow_kwargs(**kwargs):
    print(kwargs) # tutaj przekazujemy slownik i podajemy nazwy w wywolaniu funkcji

def dowolna_liczba_argumentow_przekazywanie(a, b, c):
    print(a, b, c)

def dowolna_liczba_argumentow_zwracanie(a, b, c, d):
        return a+b+c+d

def tracer(func, *pargs, **kwargs):
    print('wywolanie: ', func.__name__ )
    return func(*pargs, **kwargs)

def dowolna_liczba_argumentow_test():
    dowolna_liczba_argumentow(1, 2, 'ala ma kota', dict(key=1, val=[i for i in range(1, 5)]))
    dowolna_liczba_argumentow_kwargs(a = 'ala ma kota', b = dict(key=1, val=[i for i in range(1, 5)]), c= 'jakis dlugi test')
    # powyzszy argument wymaga nazw parametrow

    lista = ['123', 'ala ma kota', '23452345.656574', '[1,2,3,4]']
    # budujemy slownik
    d = {key: lista[idx] for idx, key in enumerate('abc')}
    dowolna_liczba_argumentow_przekazywanie(**d) #przekazujac argumenty w ten sposob nalezy zadbac o to aby ten slownik **d mial nazwy kluczy zgodne z sygnatura funkcji
    dowolna_liczba_argumentow_przekazywanie(*(1, 'Iza ma psa'), **{'c': 123.456})
    print(tracer(dowolna_liczba_argumentow_zwracanie, 1, 2, c=3, d=4))
    # mozna tez tak
    e = {key: lista[idx] for idx, key in enumerate('abcd')}
    print(tracer(dowolna_liczba_argumentow_zwracanie, **e)) # w tym przypadku trzeba zapewnic ze nazwy argumentow sa takie jak w sygnaturze funkcji
    # lub tak
    k = (10, 20, 30, 40)
    print(tracer(dowolna_liczba_argumentow_zwracanie, *k)) # w tym przypadku trzeba zapewnic ze ilosc argumentow jest taka sama

def dow_licz_arg(*args, **kwargs):
    print(args[0]) # w przypadku *args tutaj mamy liste mozemy w taki sposob przekonwertowac krotke na liste
    for i in args:
        print(i)

    for i in kwargs:
        print(i.items())

def dowolna_liczba_argumentow_test_2():
    # lista
    l = ['ala ma kota', 123.456, [34,45,67,78]]
    d = {1: 'ala ma kota', 2: 'Iza ma psa'}
    a = 123
    #dow_licz_arg(l)
    dow_licz_arg(d)
    #dow_licz_arg(a, d)
    
