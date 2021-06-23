def przyklad_generatora():  # to jest funkcja generatora
    for i in range(5):
        yield i ** 2

def przyklad_generatora_test():
    for i in przyklad_generatora():
        print(i, end=' : ')
    x = przyklad_generatora()
    print(x)
    # ale
    print(next(x)) # nexty uzywamy gdy nie uzywamy fora, bo for ma już zaszyte te nexty
    print(next(x))
    print(next(x))
    print(next(x))
    print(next(x))


    #print(next(x)) # tu zostanie ciepniety wyjatek

def przyklad_generatpra_send():
    for i in range(2, 10):
        x = (yield i % 3)
        print(x) # zwracajac yieldem x tracimy jego wartosc, stad None

# testujemy
def przyklad_generatora_send_test():
    g = przyklad_generatpra_send()
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    g.send(11) # tutaj nadajemy x wartosc 11

def wyrazenie_generatora():
    # wyrazenie generatora to taka lista skladana z nawiasami okraglymi
    y = (x ** 2 for x in range(5))
    print(y) # <generator object wyrazenie_generatora.<locals>.<genexpr> at 0x000001F11195ABA0>
    print(next(y))
    print(next(y))
    print(next(y))
    print(next(y))
    print(next(y))

def implementacja_zip_map():
    l = list(zip([1, 3, 667.9], ['ala ma kota', 'Iza ma psa', 'ola ma chomika'], [7, 9, 12])) # jeszcze raz przyklad zipa
    print(l)
    m = list(map((lambda x, y: x**y), [1,2,3], [1,2,9]))
    print(m)

    def mymap(func, *seqs):
        res = []
        for arg in zip(*seqs):
            res.append(func(*arg))
        return res
    print(mymap(pow, [1,2,3], [4,5,6]))

    # to samo w przypadku uzycia list skladanych

    def mymap2(func, *seqs):
        return [func(*args) for args in zip(*seqs)]
        # return (func(*args) for args in zip(*seqs)) # w przypadku gdy chcielibysmy wytworzyc generator
    print(mymap2(abs, [-2, -4, -6, -9, 18]))


def implementacja_zip_map_2():
    def myzip(*seqs):
        seqs = [list(s) for s in seqs]
        res = []
        while all(seqs):
            res.append(tuple(s.pop(0) for s in seqs))
        return res

    def mymap(*seq, pad=None):
        seq = [list(s) for s in seq]
        res = []
        while any(seq):
            res.append(tuple((s.pop(0) if s else pad) for s in seq))
        return res

    print(myzip('abc', 'xyz123'))
    print(mymap('abc', 'xyz123'))

    # inny sposob
    def myzip_2(*args):
        return [tuple(s[i] for s in args) for i in range(min(len(s) for s in args))]

    print(myzip_2([1, 3, 5], [7, 9, 0, 10]))
    # zmiana tych wewnetrznych tupli na wewnetrzne listy
    print([list(i) for i in myzip_2([1, 3, 5], [7, 9, 0, 10])])


    

