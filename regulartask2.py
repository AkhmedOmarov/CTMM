import ctypes
import numpy as np
from mycontextmanagers import *
import multiprocessing as mp
from multiprocessing import Pool, Array, Process, Queue


def multsequential(a, b):
    res = np.zeros((len(a), len(a[0])))
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(a[0])):
                res[i][j] += a[i][k] * b[k][j];
    return res


def multmultiprocessing(a, b):
    res = np.zeros((len(a), len(a[0])))
    #
    # def f(a, b, i, j):
    #     for k in range(len(a[0])):
    #         res[i][j] += a[i][k] * b[k][j];
    #
    # if __name__ == '__main__':
    #     with Pool(processes=4) as pool:
    #         pool.map(f, [(a, b, i, j) for i in range(len(a)) for j in range(len(b[0]))])
    return res


def multcython(a, b):
    pass


def mult(a, b, mode):
    result = 'Warning'
    if len(a[0]) != len(b):
        print('Invalid matrix dimensions: (m×n) × (n×k) = (m×k)')
    elif mode == 'sequential':
        result = multsequential(a, b)
    elif mode == 'multiprocessing':
        result = multmultiprocessing(a, b)
    elif mode == 'cython':
        result = multcython(a, b)
    else:
        print('Invalid argument value - \'mode\'')
    return result


a = np.array([[2, 0], [0, 2]])
b = np.array([[1, 2], [3, 4]])


# with time_manager():
#     print('Sequential:')
#     c = mult(a, b, 'sequential')
# print(c)
#
# with time_manager():
#     print('Multiprocessing')
#     d = mult(a, b, 'multiprocessing')
# print(d)

# a = [1, 2]
# def f(x):
#     return x[0] + x[1]
# if __name__ == '__main__':
#     with Pool(processes=2) as pool:
#         print(pool.map(f,(a,)))

def f(a):
    for i in range(len(a)):
        a[i] = i

if __name__ == '__main__':
    # arr = mp.RawArray('i', 10)
    arr = Array('i', 10)
    with Pool(2) as p:
        p.map(f, (arr,))
    # p = Process(target=f, args=(arr,))
    # p.start()
    # p.join()
    print(arr[:])
