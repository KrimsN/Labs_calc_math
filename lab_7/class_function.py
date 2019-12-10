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
    

    
    def __str__(self):
        return self.fun
        
    def plot_x(self, dx, rng=5):
        plot(self.fun, (x, dx-rng, dx+rng))
        
    def plot(self, dx1, dx2):
        plot(self.fun, (x, dx1, dx2))
