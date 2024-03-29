import numpy as np
from typing import TextIO

def check(n:int):
    

    return False

def read(input_file: TextIO, s: str):
    '''
    Чтение из файла
    '''
    if s == 'un':
        a, b = input_file.readline().split()
        a = float(a)
        b = float(b)
    else:
        X = input_file.readline().split()
        for i in range(len(X)):
            X[i] = float(X[i])

    Y = input_file.readline().split()
    for i in range(len(Y)):
        Y[i] = float(Y[i])

    if s == 'nonun':
        if len(X) != len(Y):
            raise ValueError("Lenght of X != length of Y")

    X_tests = input_file.readline().split()
    for i in range(len(X_tests)):
        X_tests[i] = float(X_tests[i])

    try:
        F_x = input_file.readline()
    except EOFError:
        if s == "un":
            return a, b, Y, X_tests, None
        elif s == "nonun":
            return X, Y, X_tests, None
    else:
        if s == "un":
            return a, b, Y, X_tests, F_x
        elif s == "nonun":
            return X, Y, X_tests, F_x