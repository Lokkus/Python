import numpy as np

def print_array(desc, arr):
    print(desc)
    print(arr)
    print()

def numpy_reshape_test():
    a = np.arange(8)
    print_array('Original array: ', a)

    b = a.reshape(2, 4)
    print_array('Modified array: ', b)

def numpy_ndarray_flat_test():
    '''This function returns a 1-D iterator over the array. It behaves similar to Python's built-in iterator.'''
    a = np.arange(8).reshape(2, 4)
    print_array('Original array: ', a)

    print('After applaying the flat function:')
    print(a.flat[5])

def numpy_flatten_test():
    '''This function returns a copy of an array collapsed into one dimension. The function takes the following parameters.'''
    a = np.arange(12).reshape(4,3)
    print_array('Original array: ', a)

    b = a.flatten()
    print_array('The flattened array is: ', b)

    b = a.flatten(order='F')
    print_array('The flattened array in F-style is: ', b)

def numpy_ravel_test():
    '''This function returns a flattened one-dimensional array. A copy is made only if needed.
    The returned array will have the same type as that of the input array.
    The function takes one parameter.'''

    a = np.arange(12).reshape(4,3)
    print_array('Original array: ', a)

    b = a.ravel()
    print_array('After applying ravel function: ', b)

    b = a.ravel(order='F')
    print_array('After applying ravel function in F-style ordering: ', b)

def numpy_transpose_test():
    a = np.arange(12).reshape(4, 3)
    print_array('Original array: ', a)

    b = np.transpose(a)
    print_array('Transposed array: ', b)

    # the same effect: a.T


def numpy_broadcast_to_test():
    a = np.arange(4).reshape(1, 4)
    print_array('The original array:', a)

    b = np.broadcast_to(a, (4,4))
    print_array('After applying the broadcast_to function:', b)

def numpy_expand_dims():
    a = np.array([[1, 2], [3, 4]])
    print_array('Array a: ', a)

    y = np.expand_dims(a, axis=0)
    print_array('Array y: ', y)

    print(f'Shape a: {a.shape}, shape y: {y.shape}')

    print('Insert axin at position 1')
    y = np.expand_dims(a, axis=1)
    print_array('Array y after inserting axis at position 1: ', y)
    print(f'a.ndim = {a.ndim}, y.ndim = {y.ndim}')

    print(f'Shape a: {a.shape}, shape y: {y.shape}')

def numpy_squezze_test():
    '''This function removes one-dimensional entry from the shape of the given array.
    Two parameters are required for this function.'''

    a = np.arange(9).reshape(1, 3, 3)
    print_array('Array a: ', a)

    y = np.squeeze(a)
    print_array('Array y: ', y)

    print(f'Shapes of a: {a.shape}, shapes of y: {y.shape}')

def numpy_concatenate_test():
    a = np.array([[1, 2, 3], [6, 5, 4], [8, 9, 0]])
    b = np.array([[10, 11, 12], [13, 14, 15], [16, 17, 18]])

    print_array('First array: a', a)
    print_array('second array: b', b)

    c = np.concatenate((a, b))
    print_array('Array after concatenate: ', c)

    c = np.concatenate((a, b), axis=1)
    print_array('Array after concatenate with axis=1: ', c)

def numpy_stacks_test():
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6], [7, 8]])
    print_array('Array a: ', a)
    print_array('Array b: ', b)

    c = np.stack((a, b), 0)
    print_array('Stack the two arrays along axis 0:', c)

    c = np.stack((a, b), 1)
    print_array('Stack the two arrays along axis 1:', c)

    # horizontal stack
    c = np.hstack((a, b))
    print_array('Horizontal stack the two arrays:', c)

    # vertical stack
    c = np.vstack((a, b))
    print_array('Vertical stack: ', c)

def numpy_split_test():
    '''This function divides the array into subarrays along a specified axis. The function takes three parameters.'''
    a = np.arange(9)

    print_array('Array a: ', a)

    b = np.split(a, 3)
    print_array('Array b splitted into 3 equal-sized subarrays: ', b)

    b = np.split(a, [4, 7])
    print_array('Split the array at positions indicated in 1-D array: ', b)

    print('hsplit test')
    a = np.arange(16).reshape(4, 4)
    print_array('Array a: ', a)

    b = np.hsplit(a, 2)
    print_array('Horizontal splitting: ', b)

    print('Vertical split')
    a = np.arange(16).reshape(4, 4)
    print_array('Array a: ', a)

    b = np.vsplit(a, 4)
    print_array('Vertical split: ', b)


def numpy_append_test():
    '''
    This function adds values at the end of an input array.
    The append operation is not inplace, a new array is allocated.
    Also the dimensions of the input arrays must match otherwise ValueError will be generated
    '''
    a = np.array([[1, 2, 3], [4, 5, 6]])
    print_array('Array a: ', a)

    b = np.append(a, [7, 8, 9])
    print_array('Array after append [7, 8, 9]: ', b)

    b = np.append(a, [[7, 8, 9]], axis=0)
    print_array('Append elements along axis 0: ', b)

    b = np.append(a, [[7, 8, 9], [10, 11, 12]], axis=1)
    print_array('Append elements along axis 1: ', b)

def numpy_insert_test():
    '''
    This function inserts values in the input array along the given axis and before the given index.
    If the type of values is converted to be inserted, it is different from the input array.
    Insertion is not done in place and the function returns a new array.
    Also, if the axis is not mentioned, the input array is flattened.
    '''

    a = np.array([[1, 2], [3, 4], [5, 6]])
    print_array('Array: ', a)

    b = np.insert(a, 3, [11, 12])
    print_array('Axis parameter not passed. The input array is flattened before insertion.', b)

    b = np.insert(a, 1, [11], axis=0)
    print_array('Broadcast along axis 0:', b)

    b = np.insert(a, 1, 11, axis=1)
    print_array('Broadcast along axis 1:', b)

    where = a
    col = 1
    data_list = [11, 12, 13]
    axis = 1 #0 = row, 1 = col
    b = np.insert(where, col, data_list, axis=axis)
    print_array('Broadcast along axis 1:', b)


def numpy_delete_test():
    a = np.arange(12).reshape(3, 4)
    print_array('Array: ', a)

    b = np.delete(a, 5)
    print_array('Array flattened before delete operation as axis not used: ', b)

    b = np.delete(a, 1, axis=1)
    print_array('Column 2 deleted:', b)

    b = np.delete(a, 2, axis=0)
    print_array('Row 2 deleted:', b)

    a = np.array([1,2,3,4,5,6,7,8,9,10])
    b = np.delete(a, np.s_[::2])
    print_array('A slice containing alternate values from array deleted:', b)

def numpy_unique_test():
    a = np.array([3,6,7,8,2,1,3,4,5,6,2,3,4,5,6,7,8])
    print_array('Array: ', a)

    b = np.unique(a)
    print_array('Unique values of first array:', b)

    u, indices = np.unique(a, return_index=True)
    print(f'Indices: {indices}')
    print(u)

    print('We can see each number corresponds to index in original array:')

    u, indices = np.unique(a, return_inverse=True)
    print_array('Indices of unique array:', indices)
    print(u)

    print('Reconstruct the original array using indices:')
    print(u[indices])


if __name__ == '__main__':
    #numpy_reshape_test()
    #numpy_ndarray_flat_test()
    #numpy_flatten_test()
    #numpy_transpose_test()
    #numpy_broadcast_to_test()
    #numpy_expand_dims()
    #numpy_squezze_test()
    #numpy_concatenate_test()
    #numpy_stacks_test()
    #numpy_split_test()
    #numpy_append_test()
    #numpy_insert_test()
    #numpy_delete_test()
    numpy_unique_test()