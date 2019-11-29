from typing import TextIO
import numpy as np

def read(fp: TextIO):

    # считываем из файла тип задачи
    # t = int(fp.readline())
    # if not (0 < t < 3):
    #     raise ValueError('Incorrect task type')

    # считываем из файла размер матрицы n
    n = int(fp.readline())

    A = np.ndarray((n, n))

    # заполняем матрицу
    for i in range(n):
        numbers = fp.readline().split()
        for j in range(n):
            A[i, j] = float(numbers[j])

    return A