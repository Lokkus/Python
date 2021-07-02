import numpy as np

def numpy_amin_amax_test():
    a = np.array([[3, 7 ,9], [1, 9, 5], [1, 2, 3]])
    print(f'Array: {a}')
    print(f'Applying amin() function: {np.amin(a, 1)}')
    print(f'Applying amin() function again: {np.amin(a, 0)}')
    print(f'Applying amax() function: {np.amax(a)}')
    print(f'Applying amax() function axis = 0 (col): {np.amax(a, axis=0)}')
    print(f'Applying amax() function axis = 1 (row): {np.amax(a, axis=1)}')

def numpy_median_test():
    '''Median is defined as the value separating the higher half of a data sample from the lower half.'''
    a = np.array([[30, 65, 70], [80, 95, 10], [50, 90, 60]])
    print(f'Array:\n {a}')
    print(f'Medial function: {np.median(a)}')
    print(f'Median function along axis 0: {np.median(a, axis=0)}')
    print(f'Median function along axis 1: {np.median(a, axis=1)}')

def numpy_mean_test():
    '''
    Arithmetic mean is the sum of elements along an axis divided by the number of elements.
    The numpy.mean() function returns the arithmetic mean of elements in the array.
    If the axis is mentioned, it is calculated along it.
    '''
    a = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])
    print(f'Our array is:\n {a}')

    print(f'Applying mean() function: {np.mean(a)}')
    print(f'Applying mean() function along axis 0: {np.mean(a, axis=0)}')
    print(f'Applying mean() function along axis 1: {np.mean(a, axis=1)}')

def numpy_average_test():
    '''
    Average: Considering an array [1,2,3,4] and corresponding weights [4,3,2,1]
    Weighted average = (1*4+2*3+3*2+4*1)/(4+3+2+1)
    '''
    a = np.array([1, 2, 3, 4])
    print(f'Array:\n {a}')
    print(f'Applying average function: {np.average(a)}')


    wts = np.array([4,3,2,1])
    print(f'Applying average function again: {np.average(a, weights=wts)}')
    print(f'Sum of weights: {np.average([1,2,3,4], weights=[4,3,2,1], returned=True)}')


def numpy_standart_deviation():
    '''
    Standard deviation is the square root of the average of squared deviations from mean
    std = sqrt(mean(abs(x - x.mean())**2)), where e.g. x = [1,2,3,4]
    '''
    print(np.std([1, 2, 3, 4]))

    #variance
    '''
    Variance is the average of squared deviations, i.e., mean(abs(x - x.mean())**2). 
    In other words, the standard deviation is the square root of variance.
    '''
    print(np.var([1,2,3,4]))

if __name__ == '__main__':
    #numpy_amin_amax_test()
    #numpy_median_test()
    #numpy_mean_test()
    #numpy_average_test()
    numpy_standart_deviation()