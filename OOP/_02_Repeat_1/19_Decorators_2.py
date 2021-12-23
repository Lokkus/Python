import time

def decorator_test():
    def decorator(cls):
        class Wrapper:
            def __init__(self, *args):
                print('Init w Wrapper')
                self.wrapped = cls(*args)

            def __getattr__(self, item):
                print('__getattr w Wrapper')
                return getattr(self.wrapped, item)

        return Wrapper

    @decorator
    class C:
        def __init__(self, x, y):
            self.attr = 'spam'

    x = C(6, 7)
    print(x.attr)


def invoke_tracer_test():
    class tracer:
        def __init__(self, func):
            self.calls = 0
            self.func = func

        def __call__(self, *args):
            self.calls += 1
            print(f'Wywolanie: {self.calls}, {self.func.__name__}')
            self.func(*args)

    @tracer
    def spam(a, b, c, d):   # spam = tracer(spam)
        print(a + b + c + d)

    spam(1, 2, 3, 4)
    spam(2, 3, 4, 5)
    spam(3, 4, 5, 6)


def invoke_tracer_test_2():
    class tracer:
        def __init__(self, func):
            self.calls = 0
            self.func = func

        def __call__(self, *args, **kwargs):
            self.calls += 1
            print(f'Wywolanie: {self.calls}, {self.func.__name__}')
            return self.func(*args, **kwargs)

    @tracer
    def spam(a, b, c):
        print(a + b + c)

    @tracer
    def eggs(x, y):
        print(x ** y)

    spam(1, 2, 3)
    spam(a=3, b=5, c=6)

    eggs(2, 16)
    eggs(4, y=5)


def measurement_of_time_test():
    class timer:
        def __init__(self, func):
            self.func = func
            self.alltime = 0

        def __call__(self, *args, **kwargs):
            start = time.perf_counter()
            result = self.func(*args, **kwargs)
            elapsed = time.perf_counter() - start
            self.alltime += elapsed
            print(f'{self.func.__name__} Elapsed: {elapsed}, Alltime: {self.alltime}')
            return result


    @timer
    def listcomp(N):
        return [x * 2 for x in range(N)]

    @timer
    def mapcall(N):
        return list(map((lambda x: x*2), range(N)))

    result = listcomp(5)
    listcomp(5000000)
    listcomp(50000000)
    listcomp(100000000)
    print(result)
    print(f'Alltime: {listcomp.alltime}')

    print('')
    result = mapcall(5)
    mapcall(5000000)
    mapcall(50000000)
    mapcall(100000000)
    print(result)
    print(f'Alltime: {mapcall.alltime}')


def decorator_arguments_test():
    def timer(label='', tracer=True):
        class Timer:
            def __init__(self, func):
                self.func = func
                self.alltime = 0

            def __call__(self, *args, **kwargs):
                start = time.perf_counter()
                result = self.func(*args, **kwargs)
                elapsed = time.perf_counter() - start
                self.alltime += elapsed
                if tracer:
                    print(f'{label}: {self.func.__name__} Elapsed: {elapsed}, Alltime: {self.alltime}')
                return result
        return Timer


    @timer(label='[ListComp ==>]')
    def listcomp(N):
        return [x * 2 for x in range(N)]

    @timer(label='[MapCall ==>]')
    def mapcall(N):
        return list(map((lambda x: x*2), range(N)))

    # tests
    for func in (listcomp, mapcall):
        print('')
        func(500000)
        func(5000000)
        func(50000000)
        print(f'Alltime {func.alltime}')

    print(f'map/comp: {round(mapcall.alltime / listcomp.alltime, 3)}')

def singleton_test():
    instances = {}
    def getInstance(aClass, *args):
        if aClass not in instances:
            instances[aClass] = aClass(*args)
        return instances[aClass]

    def singleton(aClass):
        def onCall(*args):
            return getInstance(aClass, *args)
        return onCall

    @singleton
    class Person:
        def __init__(self, name, hours, rate):
            self.name = name
            self.hours = hours
            self.rate = rate

        def pay(self):
            return self.hours * self.rate

    @singleton
    class Spam:
        def __init__(self, val):
            self.attr = val

    bob = Person('Robert', 40, 40)
    print(bob.name, bob.pay())

    anna = Person('Anna', 50, 20)
    print(anna.name, anna.pay())

    x = Spam(43)
    y = Spam(99)

    print(x.attr, y.attr)


def decorator_getattr_test():
    def Tracer(aClass):
        class Wrapper:
            def __init__(self, *args, **kwargs):
                self.fetches = 0
                self.wrapped = aClass(*args, **kwargs)

            def __getattr__(self, item):
                print(f'Sledzenie: {item}')
                self.fetches +=1
                return getattr(self.wrapped, item)

        return Wrapper

    @Tracer
    class Spam:
        def display(self):
            print('Mielonka!' * 8)

    @Tracer
    class Person:
        def __init__(self, name, hours, rate):
            self.name = name
            self.hours = hours
            self.rate = rate

        def pay(self):
            return self.hours * self.rate

    food = Spam()
    food.display()
    print([food.fetches])

    bob = Person('Robert', 40, 10)
    print(bob.name)
    print(bob.pay())

    print('')
    anna = Person('Anna', rate=100, hours=60)
    print(anna.name)
    print(anna.pay())
    print(bob.name)
    print(bob.pay())
    print([bob.fetches, anna.fetches])


def arguments_range_decorator_test():
    def rangetest(*argchecks):
        def onDecorator(func):
            if not __debug__:
                return func
            else:
                def onCall(*args):
                    for (ix, low, high) in argchecks:
                        if args[ix] < low or args[ix] > high:
                            raise TypeError(f'Argument {ix} nie miesci sie w przedziale {low}..{high}')
                    return func(*args)
                return onCall
        return onDecorator

    @rangetest((1, 0, 120))
    def persinfo(name, age):
        print(f'{name} ma {age} lat')

    @rangetest([0, 1, 31], [1, 1, 12], [2, 0, 2009])
    def birthday(D, M, Y):
        print(f'Data urodzenia: {D}/{M}/{Y}')

    class Person:
        def __init__(self, name, job, pay):
            self.job = job
            self.pay = pay

        @rangetest([1, 0.0, 1.0])
        def giveRaise(self, precent):
            self.pay = int(self.pay * (1 + precent))


    #testy
    persinfo('Robert', 45)
    birthday(31, 5, 1963)

    anna = Person('Anna', 'dev', 10000)
    anna.giveRaise(.10)
    print(anna.pay)


def arguments_range_decorator_second_version_test():
    trace = True

    def rangetest(**argchecks):
        def onDecorator(func):
            if not __debug__:
                return func
            else:
                import sys
                code = func.__code__
                allargs = code.co_varnames[:code.co_argcount]
                funcname = func.__name__

                def onCalls(*args, **kwargs):
                    positionals = list(allargs)
                    positionals = positionals[:len(args)]

                    for (argname, (low, high)) in argchecks.items():
                        if argname in kwargs:
                            if kwargs[argname] < low or kwargs[argname] > high:
                                raise TypeError(f'{funcname} argument {argname} nie miesci sie w przedziale {low}..{high}')
                        elif argname in positionals:
                            position = positionals.index(argname)
                            if args[position] < low or args[position] > high:
                                raise TypeError(f'{funcname} argument {argname} nie miesci sie w przedziale {low}..{high}')
                        else:
                            if trace:
                                print(f'Argumet {argname} ma wartosc domyslna')
                    return func(*args, **kwargs)
                return onCalls
        return onDecorator

    # @rangetest(age=(0, 120))
    # def personinfo(name, age):
    #     print(f'{name} ma {age} lat')

    @rangetest(D=(1, 31), M=(1, 12), Y=(0, 2021))
    def birthday(D, M, Y):
        print(f'Birthday = {D}/{M}/{Y}')

    #testy
    #personinfo('Robert', 42)
    birthday(1, M=5, Y=2008)



if __name__ == '__main__':
    #decorator_test()
    #invoke_tracer_test()
    #invoke_tracer_test_2()
    #measurement_of_time_test()
    #decorator_arguments_test()
    #singleton_test()
    #decorator_getattr_test()
    #decorator_getattr_test()
    #arguments_range_decorator_test()
    arguments_range_decorator_second_version_test()
