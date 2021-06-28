def fun(*args):
    for i in args:
        if type(i) == list:
            print('list')
            for index, pos in enumerate(args):
                if type(pos) == int:
                    print(index, pos)
                    args[index] = 123 # nie mozna modyfikować wartosci w ten spodob, *args przekazana jako tupla

def fun_1(**kwargs):
    for key, item in kwargs.items():
        kwargs[key] = item + 10
    return kwargs

def fun_2(a, b, c):
    return a, b, c

def kwonly(a, *b, c):
    print(a, b, c)


def fun_3(a, *b, c=1, **d):
    print(a, b, c, d)

def sumRek(L):
    '''funkcja liczy sume wszystkich elementow rekurencyjnie w liscie w ktorej moga znajdowac sie inne listy'''
    sum = 0
    for x in L:
        if not isinstance(x, list):
            sum += x
        else:
            sum += sumRek(x)
    return sum


if __name__ == '__main__':
    sl = {'dana_1': 1, 'dane_2': 2}
    l = [2, 8 , [4,5,6], 'ala ma kota']
    fun(sl, l)
    print(l)
    kw = fun_1(a=1, b=2, c=3)   # konwersja na slownik
    print(kw)

    fun_2, (1,2,3)

    kwonly(1, 2, c=3)
    fun_3(1, (4, 5, 6), 83, {'c': 4, 'x': 7})

    y = [1, [2, [3, 4]]]
    sum = sumRek(y)
    print(sum)



