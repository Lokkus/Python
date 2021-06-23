class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))
    def __str__(self):
        return '[Preson: %s, %s]' % (self.name, self.pay)

class Manager(Person):
    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus)


# Alternatywa klasy Manager z osadzaniem
class Manager_2():
    def __init__(self, name, pay):
        self.person = Person(name, 'manager', pay)  # Osadzenie obiektu Person
    def giveRaise(self, percent, bonus =.10):
        self.person.giveRaise(percent + bonus)
    def __getattr__(self, attr):
        return getattr(self.person, attr)           # Delegowanie wszystkich pozostałych atrybutów


def realistyczny_przyklad_test():
    bob = Person('Robert Zielony')
    anna = Person('Anna Czerwona', job='programistka', pay=10000)
    print(bob)
    print(anna)
    anna.giveRaise(.10)
    print(anna)
    tom = Manager('Tomasz Czarny','manager', 50000)
    tom.giveRaise(.10)
    print(tom.lastName())
    print(tom)
    print('--wszystkie trzy--')
    for obj in (bob, anna, tom):
        obj.giveRaise(.10)
        print(obj)

def realistyczny_przyklad_test_2():
    tom = Manager('Tomasz Czarny', pay=1234)
    print(tom.lastName())
    # narzedzia do introspekcji
    print(tom.__class__.__name__)
    print(list(tom.__dict__.keys()))
