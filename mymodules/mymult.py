import numpy as np
from multiprocessing import Pool
from mymodules.multcython import multcython


def mult(a, b, mode):
    result = 'Warning'
    if len(a[0]) != len(b):
        print('Invalid matrix dimensions: (m×n) × (n×p) = (m×p)')
    elif mode == 'sequential':
        result = multsequential(a, b)
    elif mode == 'multiprocessing':
        result = multmultiprocessing(a, b)
    elif mode == 'cython':
        result = multcython(a, b)
    else:
        print('Invalid argument value - \'mode\'')
    return result


def multsequential(A, B):
    m, n, p = len(A), len(A[0]), len(B[0])
    result = np.zeros((m, p), 'i')
    for i in range(m):
        for j in range(p):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
    return result


# Результирующая матрица состоит из partnumper частей,
# каждая вычисляется на одном из processnumber процессов
def multmultiprocessing(A, B):
    m, p = len(A), len(B[0])
    processnumber = 4
    partnumber = 10
    part = max(1, m // partnumber)
    with Pool(processnumber) as pool:
        result = pool.starmap(multsequential, [(A[start:min(start + part, m)], B) for start in range(0, m, part)])
    return np.array(result).reshape((m, p))