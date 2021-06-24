import numpy as np

def create_empyt_array():
    a = np.empty([3, 2], dtype=int)
    print(a)

    #create zeros array
    b = np.zeros((5,), dtype=int)
    print(b)

    # create ones array
    c = np.ones((10,), dtype=int)
    print(c)

def create_array_from_existing_data():
    x = [1, 2, 3]
    a = np.asarray(x)
    print(a)

    a = np.asarray(x, dtype=float)
    print(a)

    x = (1,2,3)
    a = np.asarray(x)
    print(a)

    x = [(1, 2, 3), (4, 5)]
    a = np.asarray(x)
    print(a)

def arange_examples():
    a = np.arange(0, 10)
    print(a)

    a = np.arange(1.1, 4.1, 0.2)
    print(a)

def linspace_examples():
    x = np.linspace(0, 20, 5)
    print(x)

    x = np.linspace(2.0, 3.0, 20) # 20 oznacza, ze ile liczb musi zostac wygenerowanych w przedziale 2.0 - 3.0
    print(x)

    x = np.linspace(2, 10, 5, dtype=int)
    print(x)


def logspace_examples():
    x = np.logspace(1.0, 2, num=10)
    print(x)


if __name__ == '__main__':
    #create_empyt_array()
    #create_array_from_existing_data()
    #arange_examples()
    #linspace_examples()
    logspace_examples()
