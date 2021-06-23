def rekurencja(L):
    if not L:
        return 0
    else:
        return L[0] + rekurencja(L[1:])

def rekurencja_2(L):
    sum = 0
    for x in L:
        if not isinstance(x, list):
            sum += x
        else:
            sum += rekurencja_2(x)
    return sum

def rekurencja_test():
    X = [1, 2, 3, 3, 4, 5, 6, 7] # to nie zadziala z zagniezdzonymi listami np [1, 2, 3, [3, 4, 5], 6, 7]
    print(rekurencja(X))
    X = [1, 2, 3, [3, 4, 5, 6], 7]
    print(rekurencja_2(X))


def posrednie_wywolanie_funkcji(a, b):
    print(a, b)

def posrednie_wywolanie_funkcji_test():
    lista = [(posrednie_wywolanie_funkcji, [1, 2, 3], 'yyy'), (posrednie_wywolanie_funkcji, [1, 2, 3], 'yyy')]
    for (func, args, args1) in lista:
        func(args, args1)

def lambda_test():
    x = (lambda a, b, c : a + b + c)
    print(x('raz', 'dwa', 'trzy'))

    def knights():
        title = 'Sir'
        action = (lambda x : title + ' ' + x)
        return action

    act = knights()
    print(act('Whatever'))

    d = {key: (lambda x : x**2) for x, key in enumerate('abcd')}
    print(d['a'](5))

    # map
    l = list(map((lambda x : x**x), [1,2,3,4]))
    print(l)

    # filter
    l = filter((lambda x: x%2), range(-5, 5)) # tutaj jesli f zwraca True to dodawane są do listy
    print(next(l))
    print(next(l))
    print(next(l))
    # lub
    l = list(filter((lambda x: x%2), range(-5, 5)))
    print(l)

