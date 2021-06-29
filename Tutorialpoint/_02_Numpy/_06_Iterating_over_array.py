import numpy as np

def nditer_test():
    '''numpy.nditer is iterator object which allows iterate over an array'''

    a = np.arange(0, 60, 5)
    a = a.reshape(3, 4)

    print('Original array is: ')
    print(a)
    print()

    print('Modified array is: ')
    for x in np.nditer(a):
        print(x, end=' ')

def transpose():
    '''How to replace rolumns with rows'''
    a = np.arange(0, 60, 5)
    a = a.reshape(3, 4)

    print('Original array is: ')
    print(a)
    print()

    print('Transpose of original array is:')
    b = a.T
    print(b)

def iteration_order():
    a = np.arange(0, 60, 5)
    a = a.reshape(3, 4)
    print('Original array is: ')
    print(a)
    print()

    print('Transpose of original array is:')
    b = a.T
    print(b)

    print('Sorted in C-stryle order: ')
    c = b.copy(order='C')
    print(c)
    for x in np.nditer(c):
        print(x, end=' ')  # printuje wierszami

    print('Sorted i F-style order: ')
    c = b.copy(order='F')
    for x in np.nditer(c):
        print(x, end=' ') # printuje kolumnami

def modify_array_values():
    a = np.arange(0, 60, 5)
    a = a.reshape(4, 3)
    print('Original array is: ')
    print(a)
    print()

    # modify each row
    for x in np.nditer(a, op_flags=['readwrite']):
        x[...] = 2*x
    print(a)
    print()

    # external loop
    for x in np.nditer(a, flags=['external_loop'], order='F'):
        print(x, end=' ')


if __name__ == '__main__':
    #nditer_test()
    #transpose()
    #iteration_order()
    modify_array_values()