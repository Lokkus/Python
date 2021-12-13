def test_properyt_old_style():
    class Person:
        def __init__(self, name):
            self._name = name

        def get_name(self):
            print('Pobieranie...')
            return self._name

        def set_name(self, name):
            print('Modyfikacja...')
            self._name = name

        def del_name(self):
            print('Usuniecie...')
            del self._name

        name = property(get_name, set_name, del_name, 'Doc example')

    bob = Person('Rob Green')
    print(bob.name)
    bob.name = 'Robert A. Green'
    print(bob.name)
    del bob.name

    print('_'*20)
    anna = Person('Anna Red')
    print(anna.name)
    print(Person.name.__doc__)


def test_decorator_alternative_method():
    class Person:
        def __init__(self, name):
            self._name = name

        @property
        def name(self):
            "Dokumentacja właściwości name"
            print('Pobieranie...')
            return self._name

        @name.setter
        def name(self, value):
            print('Modyfikacja...')
            self._name = value

        @name.deleter
        def name(self):
            print('Usuniecie...')
            del self._name

    bob = Person('Rob Green')
    print(bob.name)
    bob.name = 'Robert A. Green'
    print(bob.name)
    del bob.name

    print('_' * 20)
    anna = Person('Anna Red')
    print(anna.name)
    print(Person.name.__doc__)


def test_count_attrs():
    class PropSquare:
        def __init__(self, start):
            self.value = start

        def getX(self):
            return self.value ** 2

        def setX(self, value):
            self.value = value

        X = property(getX, setX)

    p = PropSquare(3)
    q = PropSquare(4)

    print(p.X)
    p.X = 5
    print(p.X)
    print(q.X)


if __name__ == '__main__':
    #test_properyt_old_style()
    #test_count_attrs()
    test_decorator_alternative_method()
