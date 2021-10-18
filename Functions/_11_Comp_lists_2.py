import math

def listy_skladane_przyklad(text):
    res_1 = list(map(ord, text))
    print(res_1)

    res_2 = [ord(x) for x in text]
    print(res_2)

def listy_skladane_2():
    res = [x**2 for x in range(10)]
    print(res)

    # mozna to tez zrobic za pomoca lambdy
    res_2 = list(map((lambda x: x**2), range(10)))
    print(res_2)

def listy_skladane_warunki_i_zagniezdzenia():
    res = [x for x in range(5) if x % 2 == 0]
    print(list(res))

    res_2 = filter((lambda x: x %2 == 0), range(5))
    print(list(res_2))

def listy_skladane_warunki_i_zagniezdzenia_2():
    res  = [{x: y} for x in range(5) if x % 2 == 0 for y in range(5) if y %2 == 1]
    print(res)


def mnozenie_macierzy():
    A = [[1, 2, 3],
         [1, 2, 3],
         [1, 2, 3]]

    B = [[3, 4, 5],
         [6, 7, 8],
         [1, 2, 3]]

    C = []

    z = []
    for a in range(len(A)):
        for b in range(len(A)):
            z.append(sum([A[a][x] * B[x][b] for x in range(len(A))]))
        C.append(z)
        z = []
    print(C)


def listy_skladane_czytanie_pliku():
    '''stworz na pulpicie albo gdziekolwiek plik tekstowy z zawartoscia:
    aaa,
    bbb,
    ccc
    '''
    list_1 = [line.rstrip() for line in open('/home/mk/Pulpit/sample.txt')]
    print(list_1)           # ['aaa', 'bbb', 'ccc'] bez rstrip byloby ['aaa\n', 'bbb\n', 'ccc\n']

    # to samo tyle ze z wykorzystaniem map i lambda
    list_2 = list(map((lambda line: line.rstrip()), open('/home/mk/Pulpit/sample.txt')))
    print(list_2)

    # podobna sytuacja w przypadku list krotek
    listoftuple = [('Teodor', 42, 'inzynier'), ('Teofil', 50, 'dyrektor')]
    # lub
    age = [age for (name, age, prof) in listoftuple]
    age_1 = list(map((lambda row: row[1]), listoftuple))

    print(age)
    print(age_1)






if __name__ == '__main__':
    # listy_skladane_przyklad('jakis sobie text')
    # listy_skladane_2()
    # listy_skladane_warunki_i_zagniezdzenia()
    # listy_skladane_warunki_i_zagniezdzenia_2()
    # mnozenie_macierzy()
    listy_skladane_czytanie_pliku()