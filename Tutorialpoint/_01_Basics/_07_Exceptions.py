def test_assert():
    def kelvinToFahrenheit(temperature):
        assert (temperature >= 0), 'Colder than absolute zero!'
        return ((temperature-273)*1.8) + 32
    print(kelvinToFahrenheit(100))
    print(kelvinToFahrenheit(-1))

def test_open_file():
    try:
        fo = open('folder/moj_plik2.txt', 'r')
        fo.write('jakis sobie tekst')
    except IOError:
        print("Error, can't find file or read data")
    else:
        print('Written content in the file successfully')
        fo.close()

def exeption_order():
    class B(Exception):
        pass

    class C(B):
        pass

    class D(C):
        pass

    for cls in [B, C, D]:
        try:
            raise cls()
        except D:
            print('D')
        except C:
            print('C')
        except B:
            print('B')

def test_use_all_keys_in_exception():
    def divide(x, y):
        try:
            result = x/y

        except ZeroDivisionError:
            print('Division by zero')
        except TypeError:
            print('Type error, check compatible type')
        else:
            print(f'Result is {result}')
        finally:
            print('executing finally clause')

    #testujemy
    divide(2, 1)
    divide(2, 0)
    divide('3', '1')

if __name__ == '__main__':
    #test_assert()
    #test_open_file()
    #exeption_order()
    test_use_all_keys_in_exception()