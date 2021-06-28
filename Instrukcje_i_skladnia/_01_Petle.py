def petla_while():
    ''' przyklad prostej petli while'''
    x = 10
    while x:
        x = x - 1
        if x % 2 == 0: continue
        print(x, end=' ')

def petla_for():
    for i in range(0, 10, 2):
        print(i, end=' ')

    # krotki
    T = [(1, 2), (3, 4), (5, 6)]
    for x,y in T:
        print(x, y)

    # mozemy przeksztalcic klucz - wartosc ze slownika do krotki
    a = [chr(i) for i in range(65, 75)]
    b = [i for i in range(0, 10)]
    print(a)
    d = {i: v for (i, v) in zip(a, b)}
    l = list(d.items())
    for (a, b) in d.items():
        print(a, b, end=' ')

    d = {i: v for (i, v) in zip(list(range(0, 4)), ['ala ma kota', 'iza ma psa', 'ela ma pierdolca', 'ola ma chomika'])}
    print(d)

    seq1 = 'mielonka'
    seq2 = 'biedronka'

    res = []
    for x in seq1:
        if x in seq2:
            res.append(x)
    print(res)

def test_dla_map(n):
    return n**n

def zip_i_map():
    T1, T2, T3 = (1,2,3), (4,5,6), (7,8,9)
    l = list(zip(T1, T2, T3))
    print(l)

    # map jako argument przyjmuje funkcje i sekwencje
    l = [1, 2, 3, 4, 5]
    l2 = list(map(test_dla_map, l)) # ta funkcja bedzie zwracala potegi liczb przekazanej jako argument l
    print(l2)

def enumerate_test():
    s = 'ala ma kota'
    for i, j in enumerate(s):
        print(i, j)
    E = enumerate(s)
    print(next(E)) # nomanie enumerate zwraca obiekt generatora

if __name__ == '__main__':
    petla_while()
    petla_for()
    print(test_dla_map(5))
    zip_i_map()
    enumerate_test()





