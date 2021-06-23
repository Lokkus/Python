# wywolanie dzielenia przez 0

def dzielenie_przez_zero(x, y):
    return x/y

def dodawanie_roznych_typow(x, y):
    print(x + y)

def dzielenie_przez_zero_test():
    #dzielenie_przez_zero(4, 0); # takie dzialanie na pewno wywali blad dzielenia przez 0

    try:
        dzielenie_przez_zero(5, 0)
    except ZeroDivisionError:
        print('Nie dzielimy przez zero')
    finally:
        print(dzielenie_przez_zero(5, 1))

def dodawanie_roznych_typow_test():
    try:
        dodawanie_roznych_typow(5, 'ala ma kota')
    except TypeError:
        print('Nie mozna dodawac niekompatybilnych typow')
    print('Dalsze dzialanie programu')