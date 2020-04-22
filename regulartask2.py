import numpy as np
from mycontextmanagers import *
from multiprocessing import Pool, Array


def mult(a, b, mode):
    global m, n, p
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


def multsequential(a, b):
    global m, n, p
    result = np.zeros((m, p), 'i')
    for i in range(m):
        for j in range(p):
            for k in range(n):
                result[i][j] += a[i][k] * b[k][j]
    return result


def multmultiprocessing(A, B):
    global m, n, p, threadNumber, part, mp_arr
    with Pool(threadNumber) as pool:
        pool.map(partmult, range(0, m, part))
    arr = np.frombuffer(mp_arr.get_obj(), dtype='i')
    C = arr.reshape((m, p))
    return C


def partmult(start):
    global A, B, mp_arr, part, m, n, p
    arr = np.frombuffer(mp_arr.get_obj(), dtype='i')
    C = arr.reshape((m, p))
    for i in range(start, min(start + part, m)):
        for j in range(p):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]


def multcython(a, b):
    pass



md1 = (10_000, 20_000, 15_000)
md2 = (10_000, 10_000, 10_000)
md3 = (100_000, 100_000, 100_000)
md4 = (500_000, 500_000, 500_000)
md5 = (1_000_000, 1_000_000, 1_000_000)
# На заданных размерностях работает очень долго,
# поэтому тестирую на mdcustom
mdcustom = (100, 200, 150)
(m, n, p) = mdcustom
A = np.random.randint(0, 100, (m, n))
B = np.random.randint(0, 100, (n, p))
print('A:\n', A)
print('B:\n', B)
print('Correct A×B:\n', A.dot(B), '\n')

print('- Sequential -')
with time_manager():
    C = mult(A, B, 'sequential')
print(C, '\n')

# Каждый порожденный процесс обрабатывает либо следующие part строк матрицы A,
# либо все оставшиеся строки, если их осталось меньше, чем part.
print('- Multiprocessing -')
with time_manager():
    if __name__ == '__main__':
        threadNumber = 4
        part = max(1, m // threadNumber)
        mp_arr = Array('i', m * p)
        C = mult(A, B, 'multiprocessing')
print(C)
