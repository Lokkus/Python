class Indexer:
    def __getitem__(self, item):
        return item ** 2


def test_indexer_getitem():
    X = Indexer()
    for i in range(5):
        print(X[i], end=' ')

##########################################


class Steper:
    def __getitem__(self, item):
        return self.data[item]


def test_stepper_getitem():
   s = Steper()
   s.data = 'Ala ma kota'
   for item in s:
       print(item, end='')


##########################################


class Squares:
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2


def test_squares_iter_():
    for i in Squares(1, 5):     #for wywołuje metodę iter(), która wywołuje __iter__(), każda iteracja wywołuje metodę __next__()
        print(i, end=', ')
    print()

    l = [n for n in Squares(1,6)]
    print(l)

    l = list(Squares(1, 7))
    print(l)

##########################################


class Iters:
    def __init__(self, value):
        self.data = value

    def __getitem__(self, item):
        print(f'get[{item}]', end='')
        return self.data[item]

    def __iter__(self):
        print('iter=>', end='')
        self.ix = 0
        return self

    def __next__(self):
        print('next: ', end='')
        if self.ix == len(self.data):
            raise StopIteration
        item = self.data[self.ix]
        self.ix += 1
        return item

    def __contains__(self, item):
        print('contains: ', end='')
        return item in self.data


def test_Iters():
    X = Iters([1, 2, 3, 4, 5])
    print(3 in X)
    for i in X:
        print(i, end=' | ')
    print()
    print([i**2 for i in X])
    print(list(map(bin, X)))

    I = iter(X)
    while True:
        try:
            print(next(I),end=' @ ')
        except StopIteration:
            break

##########################################


class AccessControl:
    def __init__(self, data):
        for key, val in data.items():
            self.__setattr__(key, val)

    def __getattr__(self, item):
        self.__setattr__(item, 0)


def test_AccessControl():
    d = {'jeden': 'Ala ma kota', 'dwa': 'Iza ma psa', 'trzy': 'Ola ma pierdolca'}
    a = AccessControl(d)
    print(a.osiem)
    for key, val in a.__dict__.items():
        print(f'key: {key} : val: {val}')


##########################################

if __name__ == '__main__':
    #test_indexer_getitem()
    #test_stepper_getitem()
    #test_squares_iter_()
    #test_Iters()
    test_AccessControl()