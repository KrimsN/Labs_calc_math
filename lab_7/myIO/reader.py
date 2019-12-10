from typing import TextIO
from class_function import Function
import numpy as np

def read(input_file: TextIO, g):
    '''
    Чтение из файла
    '''
    n = int(input_file.readline())
    if g == "dyn":
        a, b = input_file.readline().split()
        a, b = float(a), float(b)
        f = Function(input_file.readline())
        return n, a, b, f


    elif g == "eq":
        h = float(input_file.readline())
        Y = input_file.readline().split()
        Y = np.array(Y, dtype='float32')
        return n, h, Y



    elif g == "noneq":
        X = input_file.readline().split()
        X = np.array(X, dtype='float32')
        Y = input_file.readline().split()
        Y = np.array(Y, dtype='float32')
        return n, X, Y
            
    
