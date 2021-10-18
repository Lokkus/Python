def echo(message):
    print(message)


def check_echo():
    echo('wywolanie_bezposrednie')
    x = echo
    x('Wywolanie pośrednie')

# przekazywanie funkcji jako parametr innej funkcji + dodanie parametrow wywolania
def indirect(func, arg):
    func(arg)
    schedule = [(echo, 'Mielonka'), (echo, 'Szynka')]
    for (func, arg) in schedule:
        func(arg)

def make(label):
    def echo(message):
        print(label + ':' + message)
    return echo



if __name__ == '__main__':
    check_echo()
    indirect(echo, 'Komunikat')
    F = make('Mielonka')
    F('Szynka')
    F('Jajka')
