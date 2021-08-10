import numpy as np

def numpy_dot_test():
    '''
    This function returns the dot product of two arrays.
    For 2-D vectors, it is the equivalent to matrix multiplication.
    For 1-D arrays, it is the inner product of the vectors.
    For N-dimensional arrays, it is a sum product over the last axis of a and the second-last axis of b.
    '''
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[10, 20], [30, 40]])
    print(np.dot(a, b))


def numpy_vdot_test():
    '''
    This function returns the dot product of the two vectors.
    If the first argument is complex, then its conjugate is used for calculation.
    If the argument id is multi-dimensional array, it is flattened.
    '''

    a = np.array([[1, 2], [3, 4]])
    b = np.array([[10, 20], [30, 40]])
    print(np.vdot(a, b))

def numpy_matmul_test():
    '''
    The numpy.matmul() function returns the matrix product of two arrays.
    While it returns a normal product for 2-D arrays, if dimensions of either argument is >2,
    it is treated as a stack of matrices residing in the last two indexes and is broadcast accordingly.

    On the other hand, if either argument is 1-D array, it is promoted to a matrix by appending a 1 to its dimension,
    which is removed after multiplication.
    '''

    a = [[1, 0], [0, 1]]
    b = [[4, 1], [2, 2]]
    print(np.matmul(a, b))

if __name__ == '__main__':
    #numpy_dot_test()
    #numpy_vdot_test()
    numpy_matmul_test()