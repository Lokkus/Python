from abc import ABCMeta, abstractmethod
class Super:
    def method(self):
        print('Super.method')

    def delegate(self):
        self.action()           # to jest do zaimplementowania


class Inheritor(Super):
    pass


class Replacer(Super):
    def method(self):
        print('Replacer.method')


class Expander(Super):
    def method(self):
        print('poczatek Expander.method')
        super(Expander, self).method()
        #Super.method(self)     # da ten sam rezultat co powyżej
        print('koniec Expander.method')


class Provider(Super):
    def action(self):
        print('Provider.action')

######################################################################################################################

class Super2(metaclass=ABCMeta):
    def method(self):
        print('Super2.method')

    @abstractmethod
    def action(self):
        pass


class Provider2(Super2):
    def method(self):
        print('Provider.method')

    def action(self):
        print('Provided.action')



########################################### TESTS ####################################################################

def test_interfaces_of_class():
    x = Super()
    #x.delegate()       # to nie zadziala bo metoda action nie jest zaimplementowana
    # ale
    for klass in (Inheritor, Replacer, Expander):
        print(klass.__name__ + '...')
        klass().method()
    x = Provider()
    x.delegate()

def test_abstract_method():
    #x = Super2()           # Can't instantiate abstract class Super2 with abstract method action
    y = Provider2()
    y.action()


def x(liczba):
    suma = 0
    for a in range(len(str(liczba))):
        suma += (int(str(liczba)[a]))
    print(suma)



if __name__ == '__main__':
    #test_interfaces_of_class()
    #test_abstract_method()
    x(12345)