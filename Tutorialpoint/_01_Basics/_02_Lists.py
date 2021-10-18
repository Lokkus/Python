def listy_test():
    def tworzenie_macierzy():
        # tworze macierz
        mac = [[1, 2, 3], [6, 5, 4], [3, 7, 2]]
        print(mac[0]) # printuje pierwszy wiersz
        print(mac[2]) # printuje trzeci wiersz
        print([x[0] for x in mac])  # printuje pierwsza kolumne
        print([x[2] for x in mac])  # printuje trzecia kolumne

def wyznacznik_macierzy():
    def getMatrixMinor(m, i, j):
        x = [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]
        return x # m[:i]+m[i+1:]) oznacza pominiecie danego wiersza, row[:j] + row[j+1:] oznacza pominiecie danej kolumny


    def getDet(m):
        if len(m) == 2:
            x = m[0][0] * m[1][1] - m[1][0] * m[0][1]
            return x

        determinant = 0
        for c in range(len(m)):
            determinant += ((-1)**c)*m[0][c]*getDet(getMatrixMinor(m, 0, c))
        return determinant

    m = [[1, 2, 3], [6, 5, 4], [3, 7, 2]]
    m2 = [[1, 2, 10, 4], [5, 4, 3, 2], [7, 8, 9, 3], [7, 8, 1, 1]]
    d = getDet(m2)
    print(d)

def podstawowe_operacje_na_listach():
    # append
    l = [1, 2, 3]
    l.append(4)
    print(l)

    l1 = [5, 6, 7]
    l.append(l1) # doda l1 jako 1 element w liscie l
    print(l)

    # ale
    del l[4]
    print(l)
    l.extend(l1)
    print(l)

    # wstawiamy element do listy pod konkretnym ofsetem
    s = 'ala ma kota'
    l.insert(3, s)
    print(l)
    l.remove('ala ma kota') # w tej sytuacji mozemy usunac element z listy przez podanie zawartosci bez podania pozycji (jak w przypadku del)
    print(l)

if __name__ == '__main__':
    #wyznacznik_macierzy()
    podstawowe_operacje_na_listach()