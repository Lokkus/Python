import numpy as np

def multiplication_array():
    a = np.array([1, 2, 3, 4])
    b = np.array([10, 20, 30, 40])
    c = a*b
    print(c)

    print()

    a = np.array([[2, 1, 3], [-1, 4, 0]])
    b = np.array([[1, 3, 2], [-2, 0, 1], [5, -3, 2]])
    c = np.matmul(a, b)
    print(c)
    print()

    #albo
    c = a@b
    print(c)
    print()

    a = np.array([[1, 0], [0, 1]])
    b = np.array([1, 2])
    c = a @ b
    print(c)

def adding_array_with_broadcastring():
    a = np.array([[0, 0, 0, 0], [10, 10, 10 ,10], [20, 20, 20, 20], [30, 30, 30, 30]])
    b = np.array([1, 2, 3, 4])
    print(a)
    print(b)
    c = a + b
    print(c)

if __name__ == '__main__':
    #multiplication_array()
    adding_array_with_broadcastring()