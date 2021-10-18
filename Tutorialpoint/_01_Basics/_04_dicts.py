def compares():
    d1 = dict()
    d2 = dict()

    d1['Name'] = 'Marcin'
    d2['Name'] = 'Marcin'
    if d1 == d2:
        print('takie same')

def fromkeys_fun():
    seq = ('Name', 'Age', 'Whatever')
    d1 = dict.fromkeys(seq, 3)
    print(d1)

def items_fun():
    d1 = {'Name': 'Marcin', 'Surname': 'Mediator', 'Age': 39, 'Phone': 555666777}
    for key, val in d1.items():
        print(f'Key: {key}, Val: {val}')

if __name__ == '__main__':
    #compares()
    #fromkeys_fun()
    items_fun()