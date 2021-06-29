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

    print(a[...,2]) # print last column
    print(a[:,2]) # the same

    print(a[0,:]) # print first row
    print(a[0,...]) # the same

def advanced_slicing():
    x = np.array([[1, 2], [3, 4], [5, 6]])
    y = x[[0, 1, 2], [0, 1, 0]] #take: from row 0 elem 0, from row 1, elem 1, from row 2, elem 0
    print(x)
    print(y)

def advanced_slicing_2():
    x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
    print(x)

    #slicing
    y = x[1:, 1:]
    print(y)
    print()

    y = x[0:2, 1:2]
    print(y)
    print()
    # or using column
    y = x[1:, [1, 2]]
    print(y)


def boolean_array_indexing():
    x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
    print(x[x > 5]) # print numbers > 5


if __name__ == '__main__':
    #numpy_slice(10, 2, 7, 2)
    #multidimensional_slices()
    #advanced_slicing()
    #advanced_slicing_2()
    boolean_array_indexing()