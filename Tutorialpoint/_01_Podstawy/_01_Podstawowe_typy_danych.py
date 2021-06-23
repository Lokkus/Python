import random
import copy
import numpy as np
from itertools import product


def konwersje_test():
    # utworz slownik
    d = {}
    l = ['a', 'b', 'c', 'd']
    for i in l:
        d[i] = ord(i)
    for a, b in d.items():
        print(f'klucz = {a}, wartosc = {b}')


def losowanie_randomowe():
    '''W tej f. zwracamy liste 10 losowych wartosci typu int. Parametr rozmiaru listy moze zostac orzekazany w funkcji'''
    s = set()
    size = 10
    while len(s) <= size:
        s.add(random.randint(1, 20))

    print(s)


def funkcja_zaracajace_liczbe_z_ciagu_f_odpowiadaca_parametrowi(param):
    if param > 10 or param < 0:
        return
    p = 10 ** param
    a = 1
    b = 0
    while True:
        b = a + b
        a = b - a
        print(b)
        if (p - b) < a:
            break
    print(b)

def palindrom_string(s):
    # remove all white space and convert it to lower case
    s1 = ''.join(s.split()).lower()
    if s1 == s1[::-1]:
        print(f'Wyraz {s1} jest palindromem')

    if ''.join(s.split()).lower() == ''.join(s.split()).lower()[::-1]:
        print(f'Wyraz jest palindromem')


def split_join_zabawa():
    napis = 'ala ma kota'
    print(napis.replace('a', 'x'))
    n = napis.split() # ['ala', 'ma', 'kota'] rozwala poszczegolne elementy stringu na liste
    n1 = ''.join(napis.split())  # najprostrzy sposb na usuniecie spacji
    n2 = ''.join(napis.split('a')) # najprostrzy sposob na usuniecie literki 'a'
    print(n)
    print(n1)
    print(n2)






if __name__ == '__main__':
    # konwersje_test()
    # losowanie_randomowe()
    #funkcja_zaracajace_liczbe_z_ciagu_f_odpowiadaca_parametrowi(11)
    #palindrom_string('kobyla MA maly Bok')
    split_join_zabawa()

