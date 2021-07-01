import numpy as np

def first_example():
    a = np.array([[1, 2, 3], [6, 5, 4], [3, 7, 2]], dtype=int)
    print(a)
    print(f'Wyznacznik powyzszej macierzy: {np.linalg.det(a)}')
    print(f'get first column: {a[:, 0]}')

    x = np.linspace(0, 44.5)
    print(x)

def data_types_example():
    # file name can be used to access content of age column
    dt = np.dtype([('age', np.int8)])
    a = np.array([(10, ), (20, ), (30, )], dtype=dt)
    print(a['age'])

    # ponizszy przyklad definiuje strukture nazwana student, ten dtype jest zastosowany do obiektu ndarray
    student = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
    print(student)

    a = np.array([('student 1', 21, 4.4), ('student 2', 22, 5.0)])
    print(a)



if __name__ == '__main__':
    #first_example()
    data_types_example()