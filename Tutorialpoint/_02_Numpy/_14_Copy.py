import numpy as np
import jira



def numpy_no_copy_test():
    a = np.arange(6)
    b = a
    print(f'Array a: \n{a}\nArray b: \n{b}')
    print(f'Address of a: {hex(id(a))}\nAddress of b: {hex(id(b))}')

    b.shape = 1, 6
    print(f'Array a: \n{a}\nArray b: \n{b}') # b affects on a

def numpy_shallow_copy_test():
    a = np.arange(6).reshape(3, 2)
    b = a.view()

    print(f'Array a:\n{a}\nArray b:\n{b}')
    print(f'Address of a: {hex(id(a))}\nAddress of b: {hex(id(b))}') # addresses are not the same

    b.shape = 2, 3
    print(f'Array a:\n{a}\nArray b:\n{b}') # b doesn't affect on a


def numpy_slice_create_view_test():
    a = np.arange(6).reshape(3, 2)
    print(f'Array:\n{a}')

    s = a[:, :2]




if __name__ == '__main__':
    numpy_no_copy_test()
    #numpy_shallow_copy_test()