from Wprowadzenie.Funkcje import global_nonlocal

x = 99

# global
def fun_1():
    x = 88
    print('W funkcji zmienna lokalna x = {}, zmienna globalna x = {}'.format(x, global_nonlocal.x))

def fun_2():
    global x
    x += 100
    print('W fun_2, zmienna jest global, wynosi: {} a prawdzwa globalna: {}'.format(x, global_nonlocal.x))

# nonlocal - prosty przyklad z modyfikacja zmiennej, bez nonlocal nie da sie jej modyfikowac
def fun_3():
    z = 123
    print('W fun_3 zmienna z = {}'.format(z))
    def fun_4():
        nonlocal z
        z += z
        print('W fun_4 zmienna z = {}'.format(z))
    fun_4()

# bez nonlocal, pamietamy stan funkcji
def fun_5(z1):
    z = z1
    def fun_6(z2):
        print(z, z2)
    return fun_6

def fun_7(): # testujemy fun_5 oraz fun_6
    F = fun_5(0) # pamietamy stan, z bedzie = 0
    F('jakis string')
    F('inny string')



# main
if __name__ == "__main__":
    fun_7()