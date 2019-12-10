a, b = -5 , 5

string = '2x+2'#'x^2-8+2x'#input()

import sympy
from sympy.parsing.sympy_parser import (parse_expr,
                                        standard_transformations,
                                        implicit_application,
                                        implicit_multiplication,
                                        convert_xor)
from sympy import diff
from sympy.plotting import plot
from sympy.abc import x
from math import log10, e

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
    

    
    def plot_x(self, dx, rng=5):
        plot(self.fun, (x, dx-rng, dx+rng))
        
    def plot(self, dx1, dx2):
        plot(self.fun, (x, dx1, dx2))

from math import sqrt
phi_ = (sqrt(5)+1)/2



def dichotomy(f: Function, a: float, b: float, eps: float=1e-7):
    c = (a+b)/2
    while abs(f(c)) > eps or (b-a)/2 > eps:
        c = (a+b)/2
        if f(a)*f(c) <= 0:
            b = c
        else:
            a = c
    x_ = (b+a)/2
    return {'Name':'Метод дихотомии' ,'x*':x_, 'f(x*)': abs(f(x_)), 'eps*': (b-a)/2}


def chord(f: Function, a: float, b: float, eps: float=1e-7):
    c = (a+b)/2
    while abs(f(c)) > eps:
        
        c = a - (f(a)/(f(b)-f(a)))*(b-a)
        a = b - (f(b)/(f(a)-f(b)))*(a-b)
        if f(a)*f(c) <= 0:
            b = c
        else:
            a = c
            
        
    x_ = a - (f(a)/(f(b)-f(a)))*(b-a)
    return {'Name':'Метод хорд' ,'x*':x_, 'f(x*)': f(x_), 'eps*': abs(c-x_)/2}


def newton(f: Function, a: float, b: float, eps: float=1e-7): #Метод Ньютона
    
    if f(a)*f(a,2) > 0:
        c = a
    elif f(b)*f(b,2) > 0:
        c = b
    else:
        c = a - (f(a)/(f(b)-f(a)))*(b-a)
        
    
    while True:
        x_ = c - (f(c) / f(c,1))
        if abs(x_ - c) < eps:
            return {'Name':'Метод Ньютона' ,'x*':x_, 'f(x*)': f(x_), 'eps*': (c-x_)/2}
        c = x_


def combined(f, a, b, eps=1e-7): # Комбинированный метод
    while abs(a-b) > 2*eps:
        if f(a, 1)*f(a, 2) < 0:
            a = a - (f(a)*(a-b)) / (f(a)-f(b))
        elif f(a, 1)*f(a, 2) > 0:
            a = a - f(a)/f(a, 1)

        if f(b, 1)*f(b, 2) < 0:
            b = b - (f(b)*(b-a)) / (f(b)-f(a))
        elif f(b, 1)*f(b, 2) > 0:
            b = b - f(b)/f(b, 1)
    x_ = (a+b)/2
        
    return {'Name':'Комбинированный метод' ,'x*':x_, 'f(x*)': abs(f(x_)), 'eps*': (b-a)/2}
def iterative(): # Итеративный
    pass




def golden_section(f: Function, a: float, b: float, eps: float=1e-7): #Метод Золотого сечения
    #c = a + (b - a)/phi_
    d = b - (b - a)/phi_
    c = b - d + a
    # c - a == b - d ==>  c=b-d+a
    while abs(b-a)/2 > eps:
        
        c = a + (b - a)/phi_
        d = b - (b - a)/phi_
        #print(a,b,c,d)
        if f(a)*f(d) <= 0:
            b = d
        else: 
            a = c
    x_=(a+b)/2
    return {'Name':'Метод золотого сечения' ,'x*':x_, 'f(x*)': f(x_), 'eps*': (d-c)/2}




f = Function(string)



print(dichotomy(f, a, b))
print(chord(f, a, b))
print(newton(f, a, b))
print(golden_section(f, a, b))
print(combined(f, a, b))