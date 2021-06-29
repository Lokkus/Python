import numpy as np


def bitwise_and_test(a, b):
    print(f'Binary equivalents of {a} and {b} is {bin(a)}, {bin(b)}')
    print(f'Bitwise AND of {a} and {b}: {np.bitwise_and(a, b)}')


if __name__ == '__main__':
    bitwise_and_test(13, 17)