class Add:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Add class , value = {self.value}'

#####################################################
def test_add():
    a = Add(123)
    print(a)

#####################################################
class Commuter:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        print(f'add: {self.val} + {other}')
        return other + self.val

    def __radd__(self, other):
        print(f'radd: {self.val} + {other}')
        return other + self.val


def test_radd():
    x = Commuter(10)
    y = Commuter(20)

    print(x + 1)
    print(2 + y)
    print(x + y)

#####################################################
if __name__ == '__main__':
    #test_add()
    test_radd()