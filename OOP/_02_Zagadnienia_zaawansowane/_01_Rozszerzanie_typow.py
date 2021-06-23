###############################################################################################################
#Rozszerzanie typów za pomocą klas podrzędnych
class MyList(list):
    def __getitem__(self, item):
        print('indeksowanie %s w pozycji %s' % (self, item))
        return list.__getitem__(self, item - 1)
def rozszerzanie_typow_test():
    print(list('abc'))
    x = MyList('abc')
    print(x[1])
    print(x[3])
    x.append('cokolwiek')
    print(x)
    x.reverse()
    print(x)
###############################################################################################################