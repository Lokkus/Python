''' Bardzo podstawowy przyklad klasy'''

class C1:
    _name = None
    def __init__(self, n=None):
        self._name = n

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

def test_C1():
    k1 = C1()
    k2 = C1('Marcin')

    print(k1.get_name())
    print(k2.get_name())
    k2.set_name('Juzek')
    print(k2.get_name())

    k1._name = 'Lukasz' # jesli byloby __name  przed initem to zamiast Lukasza byly None
    print(k1.get_name())



''' Prosty przyklad polimorfizmu'''
class Employee:
    _salary = 1500
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position

    def calculate_pay_increase(self, amount):
        self._salary += amount

    def get_salary(self):
        return self._salary

class Programmer(Employee):
    def calculate_pay_increase(self, amount):
        self._salary *= amount

def test_Employee():
    p1 = Programmer('Marcin', 'Nazwisko', 'Programmer')
    p2 = Employee('Zwykly', 'Pracownik', 'Pracownik')
    p1.calculate_pay_increase(100)
    p2.calculate_pay_increase(100)
    emp = [p1, p2]
    for e in emp:
        print(e.get_salary())

if __name__ == '__main__':
    # test_C1()
    test_Employee()