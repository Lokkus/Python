import numpy as np

def numpy_slice(arange, start, stop, step):
    a = np.arange(arange)
    print(a)
    s = slice(start, stop, step)
    print(a[s])

    b = a[0:9:2]
    print(b)
    b = a[5]
    print(b)

    # slice between indexes
    print(a[2:5])

def multidimensional_slices():
    a = np.array([[1, 2, 3], [6, 5, 4], [7, 9, 2]])
    print(a)

    # slice items starting from index
    print()
    print(a[1:]) # print from 2nd row to end
    print()



if __name__ == '__main__':
    #numpy_slice(10, 2, 7, 2)
    multidimensional_slices()