
from math import sqrt
import numpy as np



def vec_eps(A, x, b):
    return A.dot(x) - b


def mat_eps(A, X):
    return A * X - np.identity(A.shape[0])


def norm(M):
    ret = 0.0
    for e in np.nditer(M):
        ret += e**2
    return sqrt(ret)

# Методы итерации предполагают, что на главной диагонали
# матрицы A находятся ненулевые элементы.
# Если это не так, то если в каждом столбце есть хотя бы один
# ненулевой элемент, то можно прибавить строку с этим эл-том
# к строке с эл-том главной диагонали, чтобы получить экви-
# валентную систему, но с ненулевым эл-том ГД.
def Solve(A: np.ndarray, b: np.ndarray, eps):
    def new_x(a, b, x):
        n = x.shape[0]
        ret = np.zeros(x.shape)
        for i in range(n):
            s1 = sum(a[i, j] * ret[j] for j in range(i))
            s2 = sum(a[i, j] * x[j] for j in range(i+1, n))
            ret[i] = b[i] + s1 + s2
        return ret

    N = A.shape[0]
    # Переходим от Ax = b к Cx = d,
    # где C = A^T * A,
    # d = A^T * b.
    A_t = A.transpose()
    C = A_t.dot(A)
    d = A_t.dot(b)

    for i in range(N):
        diag = abs(C[i, i])
        nondiag = sum(abs(C[i, j]) for j in range(N) if i != j)
        if diag <= nondiag:
            raise ValueError('Matrix not diagonally dominant')

    # начальное приближение
    x = d.copy()

    alpha = np.zeros(A.shape)
    for i in range(A.shape[0]):
        for j in range(A.shape[0]):
            alpha[i, j] = 0.0 if i == j else -C[i, j] / C[i, i]

    n = norm(alpha)
    k_eps = (1 - n)/n * eps

    beta = np.zeros(A.shape[0])
    for i in range(A.shape[0]):
        beta[i] = d[i] / C[i, i]

    xn = new_x(alpha, beta, x)
    n_diff = norm(xn - x)
    while n_diff >= k_eps:
        x = xn
        xn = new_x(alpha, beta, x)
        n_diff = norm(xn - x)

    return alpha, beta, xn