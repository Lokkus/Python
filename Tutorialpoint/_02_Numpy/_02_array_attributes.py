import numpy as np
def ndarray_shape():
    # ta funkcja zwraca tuple zawierajaca rozmiary macierzy
    a = np.array([[1, 3, 6], [6, 8, 2]])
    print(a)
    print(f'rozmiar ndarray: {a.shape}') #(2, 3) czyli 2 wiersze, 3 kolumny

    # jak zrobic resize:
    a.shape = (3, 2)
    print(a)

if __name__ == '__main__':
    ndarray_shape()