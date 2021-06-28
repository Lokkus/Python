def przypisania():
    a, b = 'napis_1', 'napis_2'
    print(a)
    print(b)

    [x, y] = ['abc', 'DEF']
    q,w,e,r = 'jaki'
    print(x)
    print(y)
    print(q)
    print(w)
    print(e)
    print(r)

    a, *b = 'napis'
    print(a)
    print(b)

def przypisanie_sekwencji():
    L = [1, 2, 3, 4]
    while L:
        front, *L = L
        print(front, L)


def wyrazenie_trojargumentowe():
    b = 5
    c = 6
    a = b if c < b else c # przyklad wyrazenia trojargumentowego
    print(a)

    # mozna jeszcze bardziej
    x = [i for i in range(0, 100) if i > 25 and i < 45 and i % 5 == 0]
    print(x)
    a = [i for i in range(0, 100) if i > 25 and i < 45 and i % 5 == 0] if c < b else 123
    print(a)

    # ogolnie jest tak: a = (zamotane wyrazenie) if warunek spelniony else (inne zamotane wyrazenie)

    a = [i for i in range(0, 100) if i % 10 == 0] if c < b else [i for i in range(20, 30)]
    print(a)

if __name__ == '__main__':
    #przypisania()
    przypisanie_sekwencji()
    #wyrazenie_trojargumentowe()
