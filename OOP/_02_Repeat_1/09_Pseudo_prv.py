class C1:
    def meth1(self): self.X = 88
    def meth2(self): print(self.X)


class C2:
    def metha(self): self.X = 99
    def methb(self): print(self.X)

class C3(C1, C2): pass


def test_class_c1_c2():
    c = C3()
    c.meth1()
    c.metha()
    print(c.__dict__) #{'X': 99}

#####################################################
class C3:
    def meth1(self): self.__X = 88
    def meth2(self): print(self.__X)


class C4:
    def metha(self): self.__X = 99
    def methb(self): print(self.__X)

class C5(C3, C4): pass


def test_class_c3_c4():
    c = C5()
    c.meth1()
    c.metha()
    print(c.__dict__)       #{'_C3__X': 88, '_C4__X': 99}
#####################################################

if __name__ == '__main__':
    #test_class_c1_c2()
    test_class_c3_c4()