# przyklad dziedziczenia diamentowego
########################################################################################3
class A(object):
    attr = 1

class B(A):
    pass

class C(A):
    attr = 2

class D(B, C):
    pass

def dziedziczenie_diamentowe_test():
    x = D()
    print(x.attr) # attr = 2 bo kolejnosz przeszukowania jest x, D, B, C
    print(dir(object))

########################################################################################3
# getattr, setattr

class Klasa:
    def __init__(self):
        self.x = 123
        self.y = 222

def get_set_test():
    k = Klasa()
    print(getattr(k, 'x'))  # wypluje 123, jesli nie ma atrybutu - wyjatek
    i = 2
    while i > 0:
        try:
            getattr(k, 'z')
        except AttributeError:
            print('nie ma atrybutu z')
            setattr(k, 'z', 666)
        else:
            print(getattr(k, 'z'))
        i -= 1

########################################################################################
#metody statyczne
class Spam:
    inst = 0
    def __init__(self):
        Spam.inst = Spam.inst + 1

    @staticmethod
    def printInst():
        print('Liczba utworzonych instancji: ', Spam.inst)


def static_test():
    a = Spam()
    b = Spam()
    c = Spam()
    a.printInst()

# inne sposoby
class Method:
    def imeth(self, x):
        print(x)

    def smeth(x):
        print(x)

    def cmeth(cls, x):
        print(cls, x)

    smeth = staticmethod(smeth)
    cmeth = classmethod(cmeth)

def static2_test():
    obj = Method()
    obj.imeth(1)

    Method.imeth(obj, 2)
    Method.smeth(3)
    obj.smeth(4)
    Method.cmeth(5)
    obj.cmeth(6)

class Kl_1:
    instancja = 0

    @classmethod
    def count(cls):
        cls.instancja += 1

    def __init__(self):
        self.count()

class Kl_2(Kl_1):
    instancja = 0
    def __init__(self):
        Kl_1.__init__(self)

class Kl_3(Kl_1):
    instancja = 0

def zliczanie_instancji_test(): # pojebane to jest
    x = Kl_1()
    y1, y2 = Kl_1(), Kl_1()
    z1, z2, z3 = Kl_3(), Kl_3(), Kl_3()

    print(x.instancja)
    print(y1.instancja)
    print(z1.instancja)


if __name__ == '__main__':
    #dziedziczenie_diamentowe_test()
    #get_set_test()
    zliczanie_instancji_test()
