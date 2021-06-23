def przyklad_funkcji():
    s1 = 'mielonka'
    s2 = 'biedronka'
    s3 = [x for x in s1 if x in s2]
    print(s3)

    # to samo ale w klasycznej funkcji
    s3 = []
    for x in s1:
        if x in s2:
            s3.append(x)
    print(s3)

x = 66

def zakres_globalny():

    z = x + 5 # w tym przypadku bierze te x wyzej
    print(z)

def zakres_globalny_2():
    global x # trzeba dac global zeby moc zmodyfikowac zmienna globalna
    print(x)
    x = 1234

def pokaz_x():
    zakres_globalny_2()
    print(x)

def f_fabryczne(N):
    def action(X):
        return X*N # tutaj mamy zapamietanie stanu
    return action

def f_fabryczne_test():
    f = f_fabryczne(3) # zapamietanie w obiekcie f wartosci 3 * X
    print(f)
    print(f(4)) # dopiero wywolanie funkcji w ten sposob, tzn z zapamietanym stanem sprawia ze winik bedzie = 12

def zakresy_zagniezdzone_lambda():
    y = 4
    a = (lambda n : y**n)
    return a

def zakresy_zagniezdzone_lambda_test():
    x = zakresy_zagniezdzone_lambda()
    print(x(2)) # wypluje 4^2

def zmienne_nonlocal(x):
    state = x
    def wew(y):
        print(state, y)
    return wew

# drugi przyklad nonlocal
def zmienne_nonlocal_2(x):
    state = x
    def wew(y):
        nonlocal state # ta zmienna musi być zawarta gdzies wewnatrz funkcji
        print(y, state)
        state += 10  # bez deklaracji nonlocal state ta linijka bylaby niemozliwa
    return wew



def zmienne_nonlocal_test():
    z = zmienne_nonlocal(5)
    z('ala ma kota')

    y = zmienne_nonlocal_2(123)
    y('Whatever')

def nonlocal_inna_wersja(start):
    def nested(label):
        nested.state = start
        print(label, nested.state, 'modyfikacja...')
        nested.state += 10
        print(label, nested.state)
    return nested

def nonlocal_inna_wersja_test():
    f = nonlocal_inna_wersja(12)
    f('ala ma kota')