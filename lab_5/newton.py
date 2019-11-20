import sympy
from sympy.parsing.sympy_parser import (parse_expr,
                                        standard_transformations,
                                        implicit_application,
                                        implicit_multiplication,
                                        convert_xor)
from sympy import diff
from sympy.plotting import plot
from sympy.abc import x
from math import log10, e, pi

class Function:
    """Класс, инкапсулирующий вычисление скалярной функции, заданной в виде строки
определенного формата"""
    def __init__(self, expr):
        # преобразования для парсера sympy
        transformations = standard_transformations + (implicit_multiplication, # умножение без знака умножения
                                                      implicit_application,  # применение скалярных ф-ий без скобок
                                                      convert_xor) # каретка как символ возведения в степень
        # замены для парсера
        replacers = {'e' : e,
                     'tg' : sympy.functions.tan,
                     'ctg' : sympy.functions.cot,
                     'lg' : sympy.Lambda(x, sympy.functions.log(x) / sympy.functions.log(10))}
        
        expr = expr.lower()
        
        self.fun = parse_expr(expr,
                              transformations = transformations,
                              local_dict=replacers)
        if self.fun.free_symbols - {x} != set():
            raise ValueError('Выражение содержит переменные кроме x')

    def __call__(self, arg, deriv=0):
        res = self.fun if deriv == 0 else self.fun.diff(*(x for i in range(0, deriv)))
        return float(res.subs({x : arg}))

    def diff(self):
        return diff(self.fun, 'x')
        
    def plot(self, dx1, dx2):
        plot(self.fun, (x, dx1, dx2))



from functools import reduce
from operator import mul
from math import factorial
import numpy as np


def product(S):
    '''Произведение чисел в последовательности S'''
    return reduce(mul, S, 1.0)


class NewtonPolynomialN:
    '''Класс объекта полинома Ньютона на неравномерной сетке'''
    
    def __init__(self, X, Y):
        '''X - табличные значения x,
        Y - табличные значения функции'''
        n = len(X)
        A = np.zeros((n,n))
        for i in range(n):
            A[i,i] = Y[i]
        for d in range(1,n):
            for k in range(n-d):
                A[k, k+d] = (A[k + 1, k + d] - A[k, k + d - 1]) / (X[k + d] - X[k])
        self.X, self.C = np.asarray(X), A[0].copy()
        

    # вычисляет функции полинома
    def phi(self, x, i, *ex):
        return product((x - self.X[j]) for j in range(i) if j not in ex)
        

    # вычисляет значение полинома или его производных (1, 2)
    def __call__(self, x, der=0):
        def d0(x):
            """ Значение полинома в точке x """
            return sum(self.C[i] * self.phi(x, i) for i in range(len(self.C)))

        def d1(x):
            res = 0.0
            for i in range(1, len(self.C)):
                res += self.C[i] * sum(self.phi(x, i, j) for j in range(i))
            return res

        def d2(x):
            res = 0.0
            for i in range(2, len(self.C)):
                for j in range(i):
                    res += self.C[i] * sum(self.phi(x, i, j, k) for k in range(i) if k != j)
            return res

        ders = [d0, d1, d2]
        try:
            return ders[der](x)
        except IndexError:
            raise ValueError(f'Derivative {der} not supported')
    
    def __str__(self):
        res = ''
        for i in range(len(self.C)):
            res += f' + {self.C[i]}' 
            for j in range(i):
                res += f' * (x - {self.X[j]})'
        return res
    
    def plot(self, X):
        Function(str(self)).plot(X[0], X[-1])


class NewtonPolynomialE:
    '''Полином Ньютона на равномерной сетке'''
    def __init__(self, a, b, Y):
        
        n = len(Y)
        A = np.zeros((n, n))
        A[0] = np.asarray(Y)
        for i in range(1, n):
            for j in range(n - i):
                A[i][j] = A[i - 1][j + 1] - A[i - 1][j]
        C = [A[i][0]/factorial(i) for i in range(n)]
    
        self.RANGE, self.C, self.h = {'a': a, 'b': b}, np.asarray(C), (b-a)/(n - 1)
        self.X = np.asarray([self.RANGE['a'] + self.h * i for i in range(n)])
        #self.New = NewtonPolynomialN(self.X, Y)

    def phi(self, q, i, *excluded):
        return product( (q-j) for j in range(i) if j not in excluded )

    def __call__(self, x, der=0):
        #return self.New(x, der)
    
        def d0(q):
            return sum(self.C[i] * self.phi(q, i) for i in range(len(self.C)))
        
        def d1(q):
            res = 0.0
            for i in range(len(self.C)):
                res += sum(self.C[i] * self.phi(q, i, j) for j in range(i))     
            return res/self.h
        
        def d2(q):
            res = 0.0
            for i in range(2, len(self.C)):
                for j in range(i):
                    res += self.C[i] * sum(self.phi(q, i, j, k) for k in range(i) if k != j)
            return res / (self.h ** 2)
            
            
    
        q = (x - self.RANGE['a'])/self.h
        
        
        ders = [d0, d1, d2]
        try:
            return ders[der](q)
        except IndexError:
            raise ValueError(f'Derivative {der} not supported')
            
    def __str__(self):
        res = ''
        for i in range(len(self.C)):
            res += f' + {self.C[i]}' 
            for j in range(i):
                res += f' * (x - {self.X[j]})/{self.h}'
        return res
    
    def plot(self, X):
        Function(str(self)).plot(X[0], X[-1])
