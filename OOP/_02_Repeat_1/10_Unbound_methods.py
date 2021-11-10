class Selfless:
    z = 5
    def __init__(self, data):
        self.data = data

    def selfless(arg1, arg2):
        return arg1 + arg2 + Selfless.z

    def normal(self, arg1, arg2):
        return self.data + arg1 + arg2 + self.z


def test_selfless():
    s = Selfless(12)
    w = s.normal(10, 20)
    print(w)
    w = Selfless.selfless(10, 20)
    print(w)
    #w = s.selfless(20, 30)     #TypeError: selfless() takes 2 positional arguments but 3 were given
    #print(w)

######################################################
class Number:
    def __init__(self, val):
        self.val = val

    def double(self):
        return self.val * 2

    def triple(self):
        return self.val * 3


def test_number():
    n = Number(10)
    for act in [n.double, n.triple]:
        print(act())
######################################################
def square(arg):
    return arg ** 2

class Sum:
    def __init__(self, val):
        self.val =val

    def __call__(self, arg):
        return self.val + arg


class Product:
    def __init__(self, val):
        self.val = val

    def method(self, arg):
        return self.val * arg


def test_bound_methods():
    sum_obj = Sum(10)
    pro_obj = Product(20)
    actions = [square, sum_obj, pro_obj.method]

    for act in actions:
        print(act(2))

    d = {act(5): act for act in actions}
    for key, val in d.items():
        print(f'{key} : {val}')

######################################################



if __name__ == '__main__':
    #test_selfless()
    #test_number()
    test_bound_methods()