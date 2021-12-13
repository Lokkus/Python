class X:
    def __getattr__(self, item):
        print('Invoke __getattr__')
        if item == 'age':
            return 40
        else:
            raise AttributeError

    def __setattr__(self, key, value):
        print('Invoke __setattr__')
        if key == 'age':
            self.__dict__['_age'] = value
        else:
            self.__dict__[key] = value


def test_get_set_attr():
    x = X()
    print(x.age)
    x.age = 41
    print(x._age)
    x.whatever = 555
    print(x.whatever)


def test_get_attr_and_get_attribute():
    class GetAttr:
        a = 1

        def __init__(self):
            self.b = 2

        def __getattr__(self, item):
            print('pobieranie ' + item)
            return 3

    x = GetAttr()
    print(x.a)
    print(x.b)
    print(x.c)


    class GetAttribute(object):
        a = 1

        def __init__(self):
            self.b = 2

        def __getattribute__(self, item):
            print('pobieranie: ' + item)
            if item == 'c':
                return 3
            else:
                return object.__getattribute__(self, item)

    x = GetAttribute()
    print(x.a)
    print(x.b)
    print(x.c)

if __name__ == '__main__':
    #test_get_set_attr()
    test_get_attr_and_get_attribute()