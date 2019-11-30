import numpy as np
from math import isclose

from polynomial import PolynomialFunction as Poly
from aberth import aberth

from functools import reduce


def get_danilevsky_mtx(A: np.ndarray):
    '''Порождает м-цу Фробениуса P и м-цы M и M^-1'''

    n = A.shape[0]

    # список матриц M
    B_l = [None for i in range(n-1)]

    # список матриц М^(-1)
    B_inv_l = [None for i in range(n-1)]

    for i in range(n-2, -1, -1):
        B_l[i] = make_B(A, i)
        B_inv_l[i] = make_B_inv(A, i)


        '''(https://vk.com/doc124637547_526415634?hash=f026d3ff2da7aba437&dl=6d88e7007fab8ac6ef стр 4)'''
        A_til = A.dot(B_l[i])
        A = B_inv_l[i].dot(A_til)

    return A, B_l, B_inv_l


def get_l_l(P):
    coefs = np.array(P[0]) * -1
    coefs = np.insert(coefs, 0, 1)
    tmp =  np.roots(coefs)
    roots = np.array([r.real for r in tmp if abs(r.imag) < 1e-4])
    roots.sort()
    print(roots)

    ret = []
    i = 0
    L = len(roots)
    while i < L:
        ret.append({'r': roots[i], 'k': 1})
        i += 1
        while i < L and abs(ret[-1]['r']-roots[i]) < 1e-4:
            i += 1
            ret[-1]['k'] += 1
    return ret







def get_lamda_list(P, eps=1e-4):

    def make_poly(P):
        '''Порождает полином из первой строки м-цы Фробениуса P'''
        return Poly([-p for p in reversed(P[0])] + [1.0])
        

    F = make_poly(P)

    roots = [r.real for r in aberth(F, eps) if abs(r.imag) < eps]
    roots.sort()
    print(roots)

    ret = []
    i = 0
    L = len(roots)
    while i < L:
        ret.append({'r': roots[i], 'k': 1})
        i += 1
        while i < L and abs(ret[-1]['r']-roots[i]) < eps:
            i += 1
            ret[-1]['k'] += 1
    return ret

def make_B(A, k):
    ''' Создаёт матрицу Mk  (https://vk.com/doc124637547_526415634?hash=f026d3ff2da7aba437&dl=6d88e7007fab8ac6ef стр 5)''' 

    if isclose(A[k+1, k], 0.0):
        raise ValueError('Unable to build Frobenius mtx')


    n = A.shape[0]
    ret = np.ndarray(A.shape)
    for i in range(n):
        for j in range(n):
            if i != k:
                ret[i, j] = 0.0 if i != j else 1.0
            elif j != k:
                ret[i, j] = - A[k+1, j] / A[k+1, k]
            else:
                ret[i, j] = 1 / A[k+1, k]
    return ret


def make_B_inv(A, k):
    ''' Создаёт матрицу Mk^(-1)  (https://vk.com/doc124637547_526415634?hash=f026d3ff2da7aba437&dl=6d88e7007fab8ac6ef стр 5)''' 

    n = A.shape[0]
    ret = np.ndarray(A.shape)
    for i in range(n):
        for j in range(n):
            if i != k:
                ret[i, j] = 0.0 if i != j else 1.0
            else:
                ret[i, j] = A[k+1, j]
    return ret


def get_S(B_l):
    '''Порождает матрицу S из матриц M1..Mn-1'''

    # reduce(np.dot, reversed(M)) =
    # = Mn-1 * Mn-2 * ... * M1
    return reduce(np.dot, reversed(B_l))


def get_frob_ver(L, n):
    '''Получение СВ для матрицы Фробениуса'''
    return np.asarray(list(L ** (n-i-1) for i in range(n)))