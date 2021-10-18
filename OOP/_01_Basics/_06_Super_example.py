class A:
    a = 1
    b = 2

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def fun(self):
        print('Jestem z klasy A')

class B(A):
    def fun(self):
        print('Wywoluje metode z klasy A ale jestem z klasy B')
        super(B, self).fun()

def temp_test():
    klasa_a = A(12, 23)
    klasa_a.fun()

    klasa_b = B(11, 22)
    klasa_b.fun()
    super(B, klasa_b.fun())

if __name__ == '__main__':
    temp_test()