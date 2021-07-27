import numpy as np

def numpy_matlib_test():
    print('Create empty matrix')
    print(np.zeros((2, 2)))

    print('Create ones matrix')
    print(np.ones((2, 2)))

    print('Create eye matrix')
    print(np.eye(3, 4, 0, dtype=float))

if __name__ == '__main__':
    numpy_matlib_test()