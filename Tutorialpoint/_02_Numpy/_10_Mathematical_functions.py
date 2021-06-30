import numpy as np

def numpy_sin_test():
    a = np.arange(0, 91, 0.1)
    s = np.sin(a*np.pi/180)
    print(s)

def numpy_cos_test():
    a = np.array([0, 30, 60, 90])
    s = np.cos(a*np.pi/180)
    print(s)

def numpy_arcsin_test():
    a = np.array([0, 30, 45, 60, 90])
    sin = np.sin(a*np.pi/180)
    print(sin)

    inv = np.arcsin(sin)
    print(inv)

    print(f'Check results converting to degrees {np.degrees(inv)}')

def numpy_rounding_test():
    a = np.array([1.00, 5.55, 123.00, 0.56, 25.53, 25.33])
    print(f'Original array: {a}')
    print(f'After rounding: {np.around(a)}')
    print(f'After rounding when decimap = 1     {np.around(a, decimals=1)}')
    print(f'After rounding when decimap = -1    {np.around(a, decimals=-1)}')


if __name__ == '__main__':
    #numpy_sin_test()
    #numpy_cos_test()
    #numpy_arcsin_test()
    numpy_rounding_test()