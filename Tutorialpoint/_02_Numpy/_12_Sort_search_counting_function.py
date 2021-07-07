import numpy as np

def numpy_sort_test(a,axis):
    print(f'Array: \n{a}')
    print(f'Apllying sort function, axis = {axis}:\n {np.sort(a, axis=axis)}')


def numpy_argsort_test():
    '''
    The numpy.argsort() function performs an indirect sort on input array,
    along the given axis and using a specified kind of sort to return the array of indices of data.
    '''

    x = np.array([3, 2, 1])
    print(f'Array: \n{x}')
    y = np.argsort(x)
    print(f'Array after argsort: \n{y}')

    print(f'Reconstruct original array in sorted order: \n{x[y]}')
    print('Reconstruct original array using loop ')
    for i in y:
        print(x[i], end=' ')

def numpy_lexsort_test():
    nm = ('raju', 'anil', 'ravi', 'amar')
    dv = ('f.y.', 's.y.', 's.y.', 'f.y.')
    ind = np.lexsort((dv, nm))

    print(f'Applying lexsort() function: \n{ind}')

    print(f'Use this index to get sorted data:\n{[nm[i] + ", " + dv[i]for i in ind]}')

def numpy_argmax_argmin_test():
    a = np.array([[10, 20, 30], [40, 1, 5], [10, 50, 34]])
    print(f'Array:\n{a}')

    print(f'Applying argmax() function: {np.argmax(a)}')
    print(f'Index of maximum number in flettened array: {a.flatten()}')

    print(f'Array containing indices of maximum along axis 1: {np.argmax(a, axis=1)}')

    print(f'Applying argmin() function: {np.argmin(a)}')
    print(f'Flattened array: {a.flatten()[np.argmin(a)]}')

def numpy_nonzero_test():
    a = np.array([[30, 0, 40], [0, 40, 50], [90, 40, 0]])
    print(f'Array:\n {a}')
    print(f'Nonzero indices: {a.nonzero()}')

def numpy_where_test():
    a = np.arange(9.).reshape(3, 3)
    print(f'Array:\n{a}')
    print(f'Indices, where element > 3\n{np.where(a > 3)}')
    print(f'Use these indices to get element satisfying the condition\n{a[np.where(a > 3)]}')

def numpy_extract_test():
    a = np.arange(9.).reshape(3, 3)
    print(f'Array:\n{a}')
    condition = np.mod(a, 2) == 0
    print(f'Element-wise value of condition\n{condition}')
    print(f'Extract elements using condition\n{np.extract(condition, a)}')

if __name__ == '__main__':
    #a = np.array([[3, 7], [9, 1]])
    #numpy_sort_test(a, axis=0)
    #numpy_sort_test(a, axis=1)
    #numpy_argsort_test()
    #numpy_lexsort_test()
    #numpy_argmax_argmin_test()
    #numpy_nonzero_test()
    #numpy_where_test()
    numpy_extract_test()