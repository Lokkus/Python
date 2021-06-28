def petla_while():
    # znaljdz liczby pierwsze w przedziale 2 : 100
    for i in range(2, 100):
        j = 2
        while j < i:
            if i % j == 0:
                break
            j += 1
        else:
            #print(i)
            pass
    # to samo ale w 1 linijce
    prime = [i for i in range(2, 10) if all(i % j for j in range(2, i))]
    t1 = [i for i in range(2, 20) if all(i % j for j in range (2, i))]
    t2 = [i for i in range(1, 50) if all([i % 3 == 0 and i % 5 == 0])]
    t3 = sum([i for i in range(100, 999) if all([i % 12 != 0 and i % 15 != 0])])
    print(prime)