import numpy as np
from typing import TextIO

def check(n:int):
    

    return False

def read(input_file: TextIO, SLE:bool):
    '''
    Чтение матрицы из файла
    '''
    n = int(input_file.readline())

    A = np.ndarray((n, n))
    if SLE:
        b = np.ndarray(n)
        #if check(n):
        #    raise ValueError("Не правильно введена матрица")
    else:
        pass


    for i in range(n):
        nums = input_file.readline().split()
        for j in range(n):
            A[i, j] = float(nums[j])
        if SLE:
            b[i] = float(nums[n])

    if SLE:
        return A, b
    else:
        return A , None

    #return task, A, b