''' lancuchy'''

def wyszukiwanie_stringu():
    s1 = 'ala ma kota'
    s2 = s1.find('ma')
    print(s2)

def palindrom():
    s1 = 'Kobyla ma maly bok'
    # usuwam biale znaki
    s1 = s1.replace(' ','')
    s1 = s1.lower()
    # odwracam string
    s2 = s1[::-1]
    if (s1 == s2):
        print('Wyraz jest palindromem')
def surowe_znaki():
    # trzeba dodac r i przydaje sie to przy sciezkach
    f = open(r'C:\Work\04_Prv\Python\Pliki\plik1_.txt', 'w') # przydaje sie w momencie gdy w nawie sciezki wystepuja takie znaki jak /n /t

def wycinki():
    s = 'abcdefghij'
    print(s[5:2:-1])

def formatowanie_stringow():
    print('Ala ma %d kotow i %d psow oraz %s' % (1, 2, 'Whatever'))
    #lub
    print('Ula ma {0} kotow {1} psow i {2} czegos'.format(1, 2, 'whatever'))

def join_przyklad():
    st = 'Ala ma kota'
    x = st.join(['1','2','3']) #1Ala ma kota2Ala ma kota3
    print(x)

def split_przyklad():
    s = 'jakis strasznie dlugi tekst'
    # dzielenie spacjami
    l = s.split(' ') # tworzy liste podzielonych stringow
    print(l)

'''Listy'''

def lista_range():
    L = list(range(-4, 4))
    print(L)
    del L[0:2]
    print(L)

def funkcja_iteracyjna(n):
    return n*n

def map_test():
    l = list(map(funkcja_iteracyjna, [1, 2, 3, 4]))
    print(l)

    l = [-i for i in l]
    print(l)
    l = list(map(abs, l))
    print(l)

'''slowiki'''
def slowniki_test():
    # sposoby kontruowania slownikow
    D = {}
    D['jajka'] = 30
    print(D)
    D = {x: x*2 for x in range(10)}
    print(D)
    print(len(D))
    D = dict(zip('Nazwa', 'Klucz')) # {'N': 'K', 'a': 'z', 'z': 'u', 'w': 'c'} zupije element po elemencie
    print(D)
    D = dict(name = 'Whatever', age = 30)
    print(D)
    D = dict(dict(some_val = 10, name='abecadlo'))
    print(D)
    D = dict.fromkeys([1,2,3,4],'abcd')
    print(D)

    D = dict(zip([1,2,3,4], ['ala', 'ma', 'kota', '123']))
    print((D))

    L = list(range(10))
    D = {x: L for x in range(10)}
    print(D)

def krotki_test():
    T1 = (0, '1', 'Test', dict(key='osiem', val='dziesiat'))
    print(T1[3])
    T2 = (1,2,3,4)
    T1 += T2
    print(T1)

def pliki():
    f = open('data.txt', 'w')
    l = ['Na dnie sargofagu noc\n', 'czarna suknia\n', 'rozrzucam korale wspomnien\n']
    f.writelines(l)
    f.close()
    f = open('data.txt', 'r')
    l2 = f.readlines();
    x = [s.rstrip() for s in l2]
    print(x)
    f.close()

    # przegladanie forem
    x = []
    for line in open('data.txt', 'r'):
        x.append(line)

