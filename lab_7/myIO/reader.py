from typing import TextIO
from class_function import Function

def read(input_file: TextIO, g):
    '''
    Чтение из файла
    '''
    n = int(input_file.readline())
    if g == "dyn":
        a, b = input_file.readline().split()
        a = float(a)
        b = float(b)
        f = Function(input_file.readline())
        return n, a, b, f
    elif g == "eq":
        h = float(input_file.readline())
        Y = input_file.readline().split()
        for i in range(Y):
            Y[i] = float(Y[i])
        return n, h, Y
    elif g == "noneq":
        h = float(input_file.readline())
        X = input_file.readline().split()
        for i in range(X):
            X[i] = float(X[i])
        Y = input_file.readline().split()
        for i in range(Y):
            Y[i] = float(Y[i])
        return n, X, Y
            
    
