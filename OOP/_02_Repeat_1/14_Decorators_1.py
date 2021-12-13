class X:
    instances = 0
    def __init__(self):
        X.instances = X.instances + 1

    @staticmethod
    def print_num_inst():
        print(f'Number of instances {X.instances}')


class Tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args):
        self.calls += 1
        print(f'call {self.calls} to {self.func.__name__}')
        self.func(*args)


def test_tracer():
    @Tracer
    def spam(a, b, c):
        print(a, b, c)

    spam(1, 2, 3)
    spam('a', 'b', 'c')
    l = [23, 34, 45]
    spam(l, 9, 0)


def test_staticmethod():
    a = X()
    b = X()
    c = X()
    a.print_num_inst()

if __name__ == '__main__':
    #test_staticmethod()
    test_tracer()