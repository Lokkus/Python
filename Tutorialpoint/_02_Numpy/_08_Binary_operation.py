import numpy as np


def bitwise_and_test(a, b):
    print(f'Binary equivalents of {a} and {b} is {bin(a)}, {bin(b)}')
    print(f'Bitwise AND of {a} and {b}: {np.bitwise_and(a, b)}')

def bitwise_or_test(a, b):
    print(f'Binary equivalents of {a} and {b} is {bin(a)}, {bin(b)}')
    print(f'Bitwise OR of {a} and {b}: {np.bitwise_or(a, b)}')

def bitwise_invert_test():
    a = np.invert(np.array([13, 14, 15], dtype=np.uint8))
    print(f'Invert of 13 where dtype of ndarray is uint8: {a}')

    print(f'Binary representation of 13: {np.binary_repr(13)}, binary representation of 242: {np.binary_repr(242)}')

def bitwise_left_shift(): # the same is right_shift
    print(f'Left shift of 10 by two positions: {np.left_shift(10, 2)}')     # 1010 << 2


if __name__ == '__main__':
    #bitwise_and_test(13, 17)
    #bitwise_or_test(13, 17)
    #bitwise_invert_test()
    bitwise_left_shift()