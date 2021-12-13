def test_property_function():
    class Powers:
        def __init__(self, square, cube):
            self._square = square
            self._cube = cube

        def getSquare(self):
            return self._square ** 2

        def setSquare(self, value):
            self._square = value

        def getCube(self):
            return self._cube ** 3

        square = property(getSquare, setSquare)
        cube = property(getCube)

    X = Powers(3, 4)
    print(X.square)
    print(X.cube)
    X.square = 5
    print(X.square)


def test_descriptions():
    class DescSquare:
        def __get__(self, instance, owner):
            return instance._square ** 2

        def __set__(self, instance, value):
            instance._square = value

    class DescCube:
        def __get__(self, instance, owner):
            return instance._cube ** 3

    class Powers:
        square = DescSquare()
        cube = DescCube()

        def __init__(self, square, cube):
            self._square = square
            self._cube = cube

    X = Powers(5, 6)
    print(X.square)
    print(X.cube)
    X.square = 7
    print(X.square)


def test_get_set_attr():
    class Powers:
        def __init__(self, square, cube):
            self._square = square
            self._cube = cube

        def __getattr__(self, item):
            if item == 'square':
                return self._square ** 2
            elif item == 'cube':
                return self._cube ** 3
            else:
                raise TypeError('error attribute ' + item)

        def __setattr__(self, key, value):
            if key == 'square':
                self.__dict__['square'] = value
            else:
                self.__dict__[key] = value

    X = Powers(5, 6)
    print(X.square)
    print(X.cube)
    X.square = 7
    print(X.square)


def test_get_attribute():
    class Powers:
        def __init__(self, square, cube):
            self._square = square
            self._cube = cube

        def __getattribute__(self, item):
            if item == 'square':
                return object.__getattribute__(self, '_square') ** 2
            elif item == 'cube':
                return object.__getattribute__(self, '_cube') ** 3
            else:
                return object.__getattribute__(self, item)

        def __setattr__(self, key, value):
            if key == 'square':
                self.__dict__['square'] = value
            else:
                self.__dict__[key] = value

    X = Powers(5, 6)
    print(X.square)
    print(X.cube)
    X.square = 7
    print(X.square)

if __name__ == '__main__':
    #test_property_function()
    #test_descriptions()
    test_get_set_attr()
    test_get_attribute()