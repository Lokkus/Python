#############################################################################################
class Employee:
    def __init__(self, name, sal=0):
        self.name = name
        self.salary = sal

    def giveRaise(self, percent):
        self.salary = self.salary + (self.salary * percent/100)

    def work(self):
        print(self.name, 'Robi rozne rzeczy')

    def getSalary(self):
        print('Po podwyzce: ', self.salary)

    def __repr__(self):
        return '<Pracownik: imie= %s, wynagrodzenie=%s>' % (self.name, self.salary)

class Chef(Employee):
    def __init__(self, name, salary=0):
        super().__init__(name, salary)

    def work(self):
        print(self.name, 'Przygotowuje jedzenie')

class Server(Employee):
    def __init__(self, name, salary=0):
        super().__init__(name, salary)

    def work(self):
        print(self.name, 'Obsluguje klienta')

class PizzaRobot(Chef):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def work(self):
        print(self.name, 'Przygotowuje pizze')

def projektowanie_z_uzyciem_klas():
    bob = PizzaRobot('Robert', 20)
    print(bob)
    bob.work()
    bob.giveRaise(percent=1)
    bob.getSalary()

    tom = Chef('Tomasz', 1000)
    john = Server('Janek', 2000)
    # tom.work()
    # tom.giveRaise(percent=12)
    # tom.getSalary()

    for o in bob, tom, john:
        o.work()
        o.getSalary()
        o.giveRaise(percent=10)
        o.getSalary()


#############################################################################################
# Programowanie zorientowane obiektowoi dziedziczenie — związek „jest”
# korzytamy w poprzednich klas
class Customer:
    def __init__(self, name):
        self.name = name

    def order(self, server):
        print(self.name, ' zamawia od ', server)

    def pay(self, server):
        print(self.name, ' placi za zamowienie ', server)

class Oven:
    def bake(self):
        print('piec piecze')

class PizzaShop:
    def __init__(self):
        self.server = Server('Ernest')
        self.chef = Chef('Robert')
        self.oven = Oven()

    def order(self, name):
        customer = Customer(name)
        customer.order(self.server)
        self.chef.work()
        self.oven.bake()
        customer.pay(self.server)

def zwiazek_jest_test():
    scene = PizzaShop()
    scene.order('Amadeusz')

#############################################################################################
# Atrybuty pseudoprywatne
class C1:
    def meth1(self):
        self.x = 99

    def meth2(self):
        print(self.x)

class C2:
    def methA(self):
        self.x = 77

    def methB(self):
        print(self.x)

class C3(C1, C2):
    pass

 # ALE !

class D1:
    def meth1(self):
        self.__x = 99

    def meth2(self):
        print(self.__x)

class D2:
    def methA(self):
        self.__x = 77

    def methB(self):
        print(self.__x)

class D3(D1, D2):
    pass

def atrybuty_pseudoprywatne_test():
    I = C3()
    I.meth1()
    I.methB() #99
    I.methA()
    I.methB() #77
    # w tym przypadku nadpisaliśmy atrybut x. Wartosc tego atrybutu bedzie rowna tyle ile zmieni go ostatnia wywolana metoda

    #############

    J = D3()
    J.meth1()
    #J.methB() #AttributeError: 'D3' object has no attribute '_D2__x' - bo odwolujemy sie do elementu ktorego jeszcze nie ma dzieki __x
    J.methA()
    J.meth2()
    J.methB()
    print(J._D1__x)

#############################################################################################
# metody zwiazane i inne obiekty wywolywalne
def square(arg):
    return arg ** 2

class Sum:
    def __init__(self, val):
        self.val = val

    def __call__(self, arg):
        return self.val + arg

class Product:
    def __init__(self, val):
        self.val = val

    def mul(self, arg):
        return self.val * arg

def metody_zwiazane_test():
    sum = Sum(10)
    product = Product(20)
    actions = [square, sum, product.mul] # do listy przekazujemy obiekty listy

    for act in actions:
        print(act(5))
    # albo
    z = [act(5) for act in actions]
    y = [j(i) for i, j in enumerate(actions)]
    print(y)
    print(z)

#############################################################################################
# wypisywanie atrybutow instancji, odczyt listy atrybutow obiektu list
class ListInstance:
    def __str__(self):
        return '<Instancja klasy %s, adres %s:\n%s' % (self.__class__.__name__, hex(id(self)), self.__attrnames())

    def __attrnames(self):
        result = ''
        for attr in sorted(self.__dict__):
            result += '\tnazwa %s=%s\n' % (attr, self.__dict__[attr])
        return result


class Super:
    def __init__(self):
        self.data1 = 'spam'

    def ham(self):
        pass

class Sub(Super, ListInstance):
    def __init__(self):
        super().__init__()
        self.data2 = 'eggs'
        self.data3 = 42

    def spam(self):
        pass

def wypisywanie_atrybutow_test():
    x = Sub()
    print(x)

    class C (ListInstance):pass
    x = C()
    x.a = 1; x.b = 2; x.c = 3
