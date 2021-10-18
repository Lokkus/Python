from functools import reduce
def inc(x):
    return x + 10


def odwzorowanie_na_map():
    counter = [12, 23, 34, 45]
    x = map(inc, counter)  # map zwraca obiekt iterowany, dlatego trzeba przekształcic to na liste zeby moc go wyswietlic
    print(list(x))
    y = map((lambda x: x * 3), counter)
    print(list(y))

def filter_example():
    x = range(-5, 6)
    y = filter((lambda y: y >=0), x)
    return y

def reduce_example(data):
    return reduce((lambda x, y: x + y), data)

def ord_owijka(wyraz):
    x = list(map(ord, wyraz))
    # albo
    y = [ord(x) for x in wyraz]
    print(x)
    print(y)

def lista_skladana_i_filter(liczba):
    x = [y for y in range(liczba) if y % 2 == 0]
    y = list(filter((lambda z: z%2 == 0), range(liczba)))
    print(x)
    print(y)


if __name__ == '__main__':
    #odwzorowanie_na_map()
    #print(list(filter_example()))

    # print(reduce_example([1,2,3,4,5]))
    # ord_owijka('ala ma kota')
    lista_skladana_i_filter(10)