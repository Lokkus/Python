class List(list):
    def __getitem__(self, item):
        print(f'Indeksowanie {self} w pozycji {item}')
        return list.__getitem__(self, item -1)

def test_List():
    x = List('abc')
    print(x)

    print(x[0])
    print(x[1])
    x.append('mielonka')
    print(x)
    x.reverse()
    print(x)

if __name__ == '__main__':
    test_List()