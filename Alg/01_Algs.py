def det_2():
    def determinant(matrix, mul):

        width = len(matrix)
        if width == 1:
            return mul * matrix[0][0]
        else:
            sign = -1
            answer = 0
            for i in range(width):
                m = []
                for j in range(1, width):
                    buff = []
                    for k in range(width):
                        if k != i:
                            buff.append(matrix[j][k])
                    m.append(buff)
                sign *= -1
                answer = answer + mul * determinant(m, sign*matrix[0][i])
        return answer

    m = [[1, 2, 3, 0], [6, 5, 4, 8], [1, 5, 9, 7], [1, 2, 8, 5]]
    print(determinant(m, 1))


def matrix_det_without_numpy_2():
    def get_matrix_minor(matrix, ix, iy):
        x = [row[:iy] + row[iy+1:] for row in matrix[:ix] + matrix[ix+1:]]
        print(f'get_matrix_minor: {x}')
        return x

    def get_matrix_det(matrix):
        if len(matrix) == 2:
            print(f'get_matrix_det: {matrix}')
            x = matrix[0][0] * matrix[1][1] - (matrix[0][1] * matrix[1][0])
            print(f'get_matrix_det: {x}')
            return x
        determinant = 0
        for i in range(len(matrix)):
            print(f'get_matrix_det: DET: {determinant}, matrix[0][{i}]: {matrix[0][i]}')
            determinant += ((-1)**i) * matrix[0][i] * get_matrix_det(get_matrix_minor(matrix, 0, i))
        return determinant

    #m = [[1, 2, 3], [7, 5, 4], [9, 8, 1]]
    m = [[1, 2, 3, 0], [6, 5, 4, 8], [1, 5, 9, 7], [1, 2, 8, 5]]
    print(get_matrix_det(m))


def sliceses():
    m = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

    #get submatrix from first row and first col m1 = [[6, 7, 8], [10, 11, 12], [14, 15, 16]]
    m1 = [col[1:] for col in m[1:]]
    print(m1)

    # get submatrix from second row and second col m2 = [[1, 3, 4], [9, 11, 12], [13, 15, 16]]
    m2 = [col[:1] + col[2:] for col in m[:1] + m[2:]]
    print(m2)

    m3 = [col[1:] for col in m[:2] + m[3:]]
    print(m3)


if __name__ == '__main__':
    #det_2()
    matrix_det_without_numpy_2()
    #sliceses()