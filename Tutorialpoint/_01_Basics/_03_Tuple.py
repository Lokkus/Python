def tuple_podstawy():
    t1 = ('ala', 'ma', 'kota')
    print(t1)
    t2 = (89,)
    print(t2)

    # w tuplach mozemy dostawac sie do poszczegolnych pozycji jak w listach
    print(t2[-1]) # bez przecinka w t2 po wpisanej wartosci, ta operacja bylaby niemozliwa
    print(t1[1:3])

    # mozemy dodawac 2 tuple
    t3 = (1, 2, 3)
    t4 = ('xyz', )
    t5 = t3 + t4
    print(t5)





if __name__ == '__main__':
    tuple_podstawy()