def why_use_metaclass_manual_way_test():
    # manual extension
    class Client1:
        def __init__(self, val):
            self.val = val

        def spam(self):
            return self.val * 2

    class Client2:
        value = 'XXXX'

    def fun_1(obj):
        return (obj.val+'_') * 4

    def fun_2(obj, value):
        return value + 'napis'

    Client1.fun_1 = fun_1
    Client1.fun_2 = fun_2

    Client2.fun_1 = fun_1
    Client2.fun_2 = fun_2

    #testy
    x = Client1('YYYYY')
    print(x.fun_1())
    print(x.fun_2('Ala ma kota '))


def why_use_metaclass_metaclass_way_test():
    #extension based on metaclass
    def fun_1(obj):
        return (obj.val+'_')*4

    def fun_2(obj, val):
        return val + ' Ala ma kota '

    class Extender(type):
        def __new__(cls, classname, supers, classdict):
            classdict['fun_1'] = fun_1
            classdict['fun_2'] = fun_2
            return type.__new__(cls, classname, supers, classdict)

    class Client1(metaclass=Extender):
        def __init__(self, val):
            self.val = val

        def spam(self):
            return self.val * 2

    # testy
    x = Client1('ABECADLO')
    print(x.spam())
    print(x.fun_1())
    print(x.fun_2('Ala ma kota'))



if __name__ == '__main__':
    why_use_metaclass_manual_way_test()
    print('METACLASS METHOD')
    why_use_metaclass_metaclass_way_test()