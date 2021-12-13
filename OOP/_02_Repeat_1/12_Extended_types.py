class List(list):
    def __getitem__(self, item):
        print(f'Indeksowanie {self} w pozycji {item}')
        return list.__getitem__(self, item -1)


class Set(list):
    def __init__(self, val=[]):
        list.__init__([])
        self.concat(val)

    def concat(self, value):
        for x in value:
            if not x in self:
                self.append(x)

    def intersect(self, other):
        res = []
        for x in self:
            if x in other:
                res.append(x)
        return res

    def union(self, other):
        res = Set(self)
        res.concat(other)
        return res

    def __and__(self, other): return self.intersect(other)
    def __or__(self, other): return self.union(other)
    def __repr__(self): return 'Zbior: ' + list.__repr__(self)


def test_List():
    x = List('abc')
    print(x)

    print(x[0])
    print(x[1])
    x.append('mielonka')
    print(x)
    x.reverse()
    print(x)


def test_set():
    x = Set([1, 3, 5, 7])
    y = Set([2, 1, 4, 5, 6])
    print(x, y, len(x))
    print(x.intersect(y))
    print(y.union(x))
    print(x & y, x | y)


if __name__ == '__main__':
    #test_List()
    test_set()