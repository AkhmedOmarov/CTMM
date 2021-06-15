import numpy as np
cimport numpy as np


cpdef np.ndarray[int, ndim=2] multcython(np.ndarray[int, ndim=2] a, np.ndarray[int, ndim=2] b):
    cdef int m = len(a)
    cdef int n =  len(a[0])
    cdef int p = len(b[0])
    cdef np.ndarray[int, ndim=2] result = np.zeros((m, p), 'i')
    cdef int i, j, k
    for i in range(m):
        for j in range(p):
            for k in range(n):
                result[i][j] += a[i][k] * b[k][j]
    return result