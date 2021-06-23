def fetcher(obj, index):
    return obj[index]

# przyklad wyjatku zdefiniowanego przez uzytkownika
class Bad(Exception):
    pass

# funkcja ktora jako wyjatek rzuca obiekt klasy Bad
def f_wykorzystujaca_klase_wyjatkow():
    raise Bad()

# kod testowy
def fetcher_test():
    # przyklad przechwytywania wyjatkow
    try:
        str = 'Ala ma kota'
        print(fetcher(str, 22))
    except IndexError:
        print('Mam wyjatek')
    finally:    # okresla to co stanie sie na koncu bez wzgledu czy wyjatek zostanie zgloszony czy nie
        print('Kontynuuje swoja prace')
        print(fetcher(str, 2))

def f_wykorzystujaca_klase_wyjatkow_test():
    try:
        f_wykorzystujaca_klase_wyjatkow()
    except Bad:
        print('Przechwycenie Bad')