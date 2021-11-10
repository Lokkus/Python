def factory(Class, *args):
    return Class(*args)

class Spam:
    def doit(self, message):
        print(message)

class Person:
    def __init__(self, name, job):
        self.name = name
        self.job = job

    def print_(self):
        print(self.name)
        print(self.job)

def test_factory():
    object1 = factory(Spam)
    object2 = factory(Person, 'Marc', 'Programmer')

    object1.doit('message')
    object2.print_()

if __name__ == '__main__':
    test_factory()