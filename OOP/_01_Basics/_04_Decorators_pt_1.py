' __call__ implementuje interfejs wywolania funkcji dla instancji klasy'

class tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print('call %s to %s ' % (self.calls, self.func.__name__))
        self.func(*args, **kwargs)

@tracer                 # Równoważne wywołaniu spam = tracer(spam)
def spam(a, b):      # Opakowanie funkcji spam w obiekt dekoratora
    for aa in a:
        print(aa)
    for bb, cc in b.items():
        print(bb, cc)

def test_tracer():
    l = [1, 2, 3]
    d = {1: 'ala', 2:'ma kota'}
    spam(l, d)

# dziedziczenie wielokrotne - kolejnosc ma znaczenie

class A:
    def __str__(self):
        print('Oto klas A')

class B:
    def __str__(self):
        print('Oto klasa B')

class C(A, B) : pass
class D(B, A) : pass

def kolejnosc_dziedziczenie_test():
    x = C()
    y = D()
    print(x.__str__())
    print(y.__str__())

if __name__ == '__main__':
    test_tracer()
    kolejnosc_dziedziczenie_test()
