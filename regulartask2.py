import numpy as np
from mycontextmanagers import time_manager
from mymult import mult
# from multcython import *


def get_mean(x):
    return sum(x)/len(x) if len(x) != 0 else 0


# На размерностях из задания работает очень долго,
# поэтому тестирую на mdcustom
md1 = (10_000, 20_000, 15_000)
md2 = (10_000, 10_000, 10_000)
md3 = (100_000, 100_000, 100_000)
md4 = (500_000, 500_000, 500_000)
md5 = (1_000_000, 1_000_000, 1_000_000)
mdcustom = (100, 200, 150)
(m, n, p) = mdcustom
A = np.random.randint(0, 100, (m, n), 'i')
B = np.random.randint(0, 100, (n, p), 'i')
# print('A:\n', A)
# print('B:\n', B)
# print('Correct A×B:\n', A.dot(B), '\n')

times = 3
timesequential = []
timemultiprocessing = []
timecython = []
for i in range(times):
    print('> Sequential:')
    with time_manager(timesequential):
        C = mult(A, B, 'sequential')
    # print(C, '\n')

    print('> Multiprocessing:')
    with time_manager(timemultiprocessing):
        if __name__ == '__main__':
            C = mult(A, B, 'multiprocessing')
    # print(C, '\n')

    print('> Cython:')
    with time_manager(timecython):
        C = mult(A, B, 'cython')
    # print(C, '\n')

print(f'> (m×n) × (n×p) = (m×p), where m = {m}, n = {n}, p = {p}')
print('> Mean values:')
print(f'Sequential      = {get_mean(timesequential)}')
print(f'Multiprocessing = {get_mean(timemultiprocessing)}')
print(f'Cython          = {get_mean(timecython)}')
