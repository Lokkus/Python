f = lambda x, y, z: x + y + z

#inny przykald
def knights():
    title = 'Sir'
    action = lambda x: title + ' ' + x
    return action

def power():
    L = [(lambda x: x**2), (lambda x: x**3), (lambda x: x**4)]
    for f in L:
        print(f(2))

def lower(str_1, str_2):
    return(lambda str_1=str_1, str_2=str_2: str_1 if str_1 < str_2 else str_2)


if __name__ == '__main__':
    # print(f(2, 3, 4))
    act = knights()
    # print(act('Robin'))
    #power()
    # a = lower('ula', 'ela')
    print(act)