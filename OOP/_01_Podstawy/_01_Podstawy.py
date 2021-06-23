class FirstClass:
    def setData(self, value):
        self.data = value
    def display(self):
        print(self.data)

class SecondClass(FirstClass):
    def display(self):
        print('cokolwiek', self.data)

class ThirdClass(SecondClass):
    def __init__(self, value):
        self.data = value
    def __add__(self, other):
        return ThirdClass(self.data + other)
    def __str__(self):
        return '[ThirdClass: %s]' % self.data
    def mul(self, other):
        self.data *= other

def first_class_test():
    f = FirstClass()
    f.setData(['ala ma kota', {1: 456.778}])
    f.display()

def second_class_test():
    s = SecondClass()
    s.setData([{'12': [12,23,34,45]}, 'Jakis sobie test'])
    s.display()

def third_class_test():
    t = ThirdClass('abc')
    t.display()
    print(t)
    b = t + 'ala ma kota'
    b.display()
    t.mul(3)
    print(t)