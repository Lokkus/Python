from more_itertools.more import seekable


def przyklad_generatora(n):
    for i in range(n):
        yield i ** 2

def wykorzystanie_przykladu_generatora(x):
    for i in przyklad_generatora(x):
        print('i = {}'.format(i))

def generator_next():
    a = przyklad_generatora(10)
    print(a)
    print(a.__next__())
    print(a.__next__())
    print(a.__next__())

def przyklad_funkcji_send():
    for i in range(10):
        X = yield i+10
        print(X)
        #print(i)

def wywolanie_przyladu_send():
    G = przyklad_funkcji_send()
    next(G)
    G.send(123)
    G.send(155)

def wyrazenia_generatorow():
    X = (x**2 for x in range(5))
    print(X)
    print(next(X))
    print(next(X))
    print(next(X))

def emulacja_map(func, *seq):
    res = []
    for args in zip(*seq):
        # print(args) # jezeli przekazemy taka sekwencje: [1, 2, 3], [4, 6, 7], [7, 8, 9] otrzymamy: (1, 4, 7) (2, 6, 8) (3, 7, 9)
        res.append(func(*args))
    return res

def emulacja_map_2(func, *args):
    # to samo co wyzej tylko po pythonowemu
    return [func(*arg) for arg in zip(*args)]

def emulacja_zip(*args):
    # tworzy liste tupli. Kazda tupla zawiera pare kolejnych elemenotw argumentow przekazanych do funkcji.
    args = [list(s) for s in args]
    print(args)
    res = []
    while all(args):
        res.append(tuple(s.pop(0) for s in args))
    return res

def emulacja_zip_pad(*args, pad=None):
    args = [list(a) for a in args]
    res = []
    # zwroc uwage ze tutaj jest any a nie all
    while any(args):
        res.append(tuple((arg.pop(0) if arg else pad) for arg in args))
    return res

def emulacja_zip_alternatywna(*args):
    minlen = min(len(arg) for arg in args)
    # res = []
    # x = ()
    # for i in range(minlen):
    #     for arg in args:
    #         x = x + (arg[i], )
    #     res.append(x)
    #     x = ()
    # to samo tylko w 1 linijce
    return [tuple(arg[i] for arg in args) for i in range(minlen)]

def emulacja_zip_3(*args):
    iters = list(map(iter, args))
    while iters:
        res = [next(i) for i in iters]
        yield tuple(res)


def generowanie_wynikow_we_wbudowanych_typach():
    D = {'a': 1, 'b': 2, 'c':3}
    x = iter(D)
    print(next(x))

def generatory_slowniki():
    # zbiory
    lista = [1, 2, 3, 4, 5]
    z = {x**2 for x in lista}
    print(z)
    d = {key: val for (key, val) in zip([1, 2, 3], [4, 5, 6, 7])}
    print(d) # d = {1: 4, 2: 5, 3: 6}



if __name__ == '__main__':
    #wykorzystanie_przykladu_generatora(5)
    # generator_next()
    # wywolanie_przyladu_send()
    # wyrazenia_generatorow()
    # print(emulacja_map(pow, [1, 2, 3], [4, 6, 7]))
    # print(emulacja_map_2(pow, [1, 2, 3], [4, 6, 7]))
    # emulacja_zip('ala', 'makota')
    # print(emulacja_zip_pad('ala', 'makota', pad=99))
    # emulacja_zip_alternatywna('ala', 'makota', 'iza', 'mapsa')
    # generowanie_wynikow_we_wbudowanych_typach()
    # print(list(emulacja_zip_3('ala', 'makota')))
    generatory_slowniki()
