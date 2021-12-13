# about __get__ and __set__

def test_descriptor():
    class Name:
        def __get__(self, instance, owner):
            print('Pobieranie...')
            return instance._name

        def __set__(self, instance, value):
            print('Modyfikacja...')
            instance._name = value

        def __delete__(self, instance):
            print('Usuniecie')
            del instance._name

    class Person:
        def __init__(self, name):
            self._name = name
        name = Name()

    bob = Person('Robert Green')
    print(bob.name)

    bob.name = 'Robert A Zielony'
    print(bob.name)
    del bob.name


if __name__ == '__main__':
    test_descriptor()