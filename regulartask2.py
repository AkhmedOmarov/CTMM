import numpy as np
from mycontextmanagers import time_manager
from mymult import mult


# На размерностях из задания работает очень долго,
# поэтому тестирую на mdcustom
md1 = (10_000, 20_000, 15_000)
md2 = (10_000, 10_000, 10_000)
md3 = (100_000, 100_000, 100_000)
md4 = (500_000, 500_000, 500_000)
md5 = (1_000_000, 1_000_000, 1_000_000)
mdcustom = (40, 80, 60)
(m, n, p) = mdcustom
A = np.random.randint(0, 100, (m, n))
B = np.random.randint(0, 100, (n, p))
# print('A:\n', A)
# print('B:\n', B)
# print('Correct A×B:\n', A.dot(B), '\n')

print('> Sequential:')
with time_manager():
    C = mult(A, B, 'sequential')
# print(C, '\n')

print('> Multiprocessing:')
with time_manager():
    if __name__ == '__main__':
        C = mult(A, B, 'multiprocessing')
# print(C, '\n')

print('> Cython:')
with time_manager():
    C = mult(A, B, 'cython')
# print(C, '\n')

