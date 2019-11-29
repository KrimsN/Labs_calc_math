from polynomial import PolynomialFunction as Poly
from numpy import random
from math import sin, cos, pi


random.seed()

def upper_bound(P: Poly):
    max_abs = max(abs(c) for c in P[:-1])
    return 1 + max_abs / abs(P[-1])


def lower_bound(P: Poly):
    return 0.0


def aberth(P: Poly, eps: float = 1e-11):
    def offsets(X):
        def offset(X, i):
            rel = P(X[i]) / P(X[i], 1)
            s = sum(1/(X[i]-X[j]) for j in range(len(X)) if i != j)
            return rel / (1 - rel * s)
        return [offset(X, i) for i in range(len(X))]

    def get_random(a, b):
        magnitude = random.uniform(a, b)
        angle = random.uniform(0, 2 * pi)
        return complex(magnitude * cos(angle), magnitude * sin(angle))

    random.seed()

    U = upper_bound(P)
    L = lower_bound(P)

    X = [get_random(L, U) for i in range(P.degree)]
    W = offsets(X)

    while not all(abs(w) < eps/2 for w in W):
        X = [x - w for x, w in zip(X, W)]
        W = offsets(X)
    X = [x - w for x, w in zip(X, W)]
    return X
