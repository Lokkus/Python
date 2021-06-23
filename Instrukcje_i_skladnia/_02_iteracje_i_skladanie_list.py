import math
def wczytanie_tresci_pliku_z_uzyciem_iteratora():
    for line in open('date.txt'): # niejawne wywolanie funkcji next()
        print(line.upper(), end=' ')

def iterowanie():
    L = [i for i in range(0, 10)]
    I = iter(L)
    while True:
        try:
            x = next(I)
        except StopIteration:
            print('Stop iteration')
            break
        print(x**2, end=' ')

def listy_skladane_1():
    f = open('date.txt', 'r')
    lines = f.readlines()
    print(lines)
     #ale
    lines = [line.rstrip() for line in lines]
    print(lines)

    #lub

    lines2 = [line[:-1] for line in lines] # to jest o tyle niebezpieczne ze wyjebuje ostani znak ktory nie zawsze jest \n
    print(lines2)

    # rozszerzona skladnia list skladanych
    f = open('date.txt', 'r')
    lines3 = f.readlines()
    print(lines3)
    lines = [line.rstrip() for line in lines3 if line[0] == 'J']
    print(lines)

    # lepiej
    lines = [line.rstrip() for line in open('date.txt') if line[0] == 'J']
    print(lines)

    # jeszcze inaczej
    lines = list(map(str.rstrip, open('date.txt')))
    print(lines)
def fun_filter(a):
    a = a if a < 5 else 0
    return a

def filter_test():
    l = ['123', '', 1234, dict(key=(1, 2, 3),val=[6, 7, 8])]
    l2 = list(filter(bool, l)) # wypiepsza wszystkie puste pozycje
    print(l2)

    l = [1,2,3,4,5,6,7,8,9]
    l2 = list(filter(fun_filter, l))
    print(l2)





