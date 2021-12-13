#basic
def test_args():

    # *args to krotka
    def _args(*args):
        print(args)
    _args(1, 2, 3, 4)
    _args()
    _args('ala ma kota', 'whatever')


# test kwargs basic
def test_kwargs():
    def _kwargs(**kwargs):
        for a, b in kwargs.items():
            print(f'KEY: {a}, VAL: {b}')
    d = {x: ['whatever'] for x in range(1, 5)}
    _kwargs(x=d)
    _kwargs(a=1, b=2)


#test unpacked args
def test_unpacked():
    def _unpacked(a, b, c, d):
        print(a, b, c, d)

    args = (1, 2)
    args += (3, 4)
    _unpacked(*args)

    args = {'a': 1, 'b':2, 'c': 3}
    #_unpacked(**args) #TypeError: _unpacked() missing 1 required positional argument: 'd'
    args['d'] = 4
    _unpacked(**args)
    # few combinations
    _unpacked(*(10, 20), **{'d': 30, 'c': 100})
    _unpacked(1, c=40, *(2, ), **{'d': 44})


def test_tracer():
    def tracker(func, *args, **kwargs):
        print(f'wywolanie: {func.__name__}')
        return func(*args, **kwargs)

    def func(a, b, c, d):
        return a + b + c + d

    print(tracker(func, 1, 2, c=3, d=4))



if __name__ == '__main__':
    #test_args()
    #test_kwargs()
    #test_unpacked()
    #test_unpacked()
    test_tracer()