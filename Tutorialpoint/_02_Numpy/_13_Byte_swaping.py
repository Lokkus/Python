import numpy as np
def numpy_byteswap_test():
    '''The numpy.ndarray.byteswap() function toggles between the two representations: bigendian and little-endian'''
    a = np.array([1, 255, 256, 65534])
    print(f'Array:\n{a}')

    print(f'Representation of data in memory in hexidecimal form: \n{list(map(hex, a))}')
    print(f'Applying byteswap() function:\n{a.byteswap(True)}')
    print(f'In hex: \n{list(map(hex, a))}')


if __name__ == '__main__':
    numpy_byteswap_test()