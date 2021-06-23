# Konstruktory i wyrażenia — __init__ i __sub__
class Number:
    def __init__(self, num):
        self.data = num
    def __sub__(self, other):
        return Number(self.data - other)


def przeladowany_operator_sub():
    X = Number(10)
    Y = X - 2 # bez __sub__ nie byloby to mozliwe
    print(Y.data)

#####################################################################################################################
# Indeksowanie i wycinanie — __getitem__ i __setitem__
class Indexer:
    def __getitem__(self, item):  # przeladowanie []
        return item**2

class IndexerSlice:
    l = []
    def __init__(self, li):
        self.l = li
    def __getitem__(self, item):
        print('getitem', item)
        return self.l[item]


def test_getitem():
    x = Indexer()
    for i in range(10):
        print(x[i], end = ' ')

def test_getitem_slice():
    l = [1,2,3,4,5,6]
    x = IndexerSlice(l)
    print(x[0])
    print(x[-1])
    print(x[2:4])
    print(x[::2])

#####################################################################################################################
# iteratory zdefiniowane przez uzytkownika
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

    def next(self):
        return self.__next__()

def test_squares():
    for i in Squares(1, 5):
        print(i, end=' ')
#####################################################################################################################
# test przynaleznosci
class Iters:
    def __init__(self, val):
        self.data = val

    def __getitem__(self, item):
        print('get[%s]' % item, end='')
        return self.data[item]

    def __iter__(self):
        print('iter=> ', end='')
        self.ix = 0
        return self

    def __next__(self):
        print('next:', end='')
        if self.ix == len(self.data):
            raise StopIteration
        item = self.data[self.ix]
        self.ix += 1
        return item

    def __contains__(self, item):
        print('contains: ', end='')
        return item in self.data

def test_iters():
    x = Iters([1, 2, 3, 4, 5, 6, 7, 8])
    print(3 in x)
    for i in x:
        print(i, end=' | ') # iter=> next:1 | next:2 | next:3 | next:4 | next:5 | next:6 | next:7 | next:8 | next:
    print()
    print([i**2 for i in x]) # ter=> next:next:next:next:next:next:next:next:next:[1, 4, 9, 16, 25, 36, 49, 64]

    I = iter(x)
    while True:
        try:
            print(next(I), end=' @ ') # next:1 @ next:2 @ next:3 @ next:4 @ next:5 @ next:6 @ next:7 @ next:8 @ next:Stop iteration
        except StopIteration:
            print('Stop iteration')
            break
#####################################################################################################################

# Emulowanie prywatności w atrybutach instancji
class PrivateExc(Exception): pass

class Privacy:
    def __setattr__(self, key, value):
        if key in self.privates:
            raise PrivateExc(key, self)
        else:
            self.__dict__[key] = value

class Test1(Privacy):
    privates = ['age']

class Test2(Privacy):
    privates = ['name', 'pay']
    def __init__(self):
        self.__dict__['name'] = 'Amadeusz'

def emulowanie_prywatnosci_test():
    x = Test1()
    y = Test2()

    x.name = 'Edward' # tu mozna dac wszystko oprocz x.age
    # y.name = 'Ernest' #line 114, in __setattr__ raise PrivateExc(key, self)

    y.age = 30 # tu mozna dac wszystko oprocz y.name y.pay
    # x.age = 40 # to samo line 114, in __setattr__ raise PrivateExc(key, self)
    # tu chodzi o to ze jezeli nazwa jest na liscie ( w przypadku Test1 to jest 'age' w przypadku Test2 to jest 'name'
    # i 'pay' to wtedy wyjebuje wyjatek

#####################################################################################################################
# Metoda __call_ przechwytuje wywołania, chodzi o to ze obiekto moze byc wywolany jak funkcja
class Callee:
    def __call__(self, *args, **kwargs):
        print('Wywolanie:', args, kwargs) # pamietaj args to krotka, kwargs to slownik ktort wymaga nazwy parametrow

def callee_test():
    c = Callee()
    c(1,2,3)
    c([2, 3, 4], 'ala ma kota', x = 123, y={5: 'piec'})