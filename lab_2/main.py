import numpy as np
import scipy.linalg
#from pprint import pprint
from Accurate_methods.LU_decomposition import Solve_SLE as Solve, inverse as inv, determinant as det

from myIO import reader, writer


if __name__ == "__main__":

    in_f = open('input.txt')

    read = reader.read(in_f, True)
    myA = read[0]
    myB = read[1]
    # myA = [[20.9, 1.2, 2.1, 0.9], [1.2, 21.2, 1.5, 2.5],[2.1, 1.5, 19.8, 1.3], [0.9, 2.5, 1.3, 32.1]]
    # myB = [21.7, 27.46, 28.76, 49.72]
    # myA = [
    # [ 1.0, -2.0,  3.0,  -4.0],
    # [ 3.0,  3.0, -5.0,  -1.0],
    # [ 3.0,  0.0,  3.0, -10.0],
    # [-2.0,  1.0,  2.0,  -3.0]
    # ]
    
    # myB = [
    #     2.0,
    #     -3.0,
    #     8.0,
    #     5.0
    # ]


    b = np.array(myB)
    A = np.array(myA)
    Det = det(A) # нахождение определителя
    print('\n\ndet_PLU: ', Det)
    #print('\n\ndet: ',scipy.linalg.det(A))

    print('\nMy\n')
    X, Y, R, NR = Solve(A, b) # X - вектор решения, Y - временный вектор, R - вектор невязка, NR - норма вектора невязки
    # print('x* = ', X)
    # print('y = ', Y)
    # print('r = ', R)
    # print('||r|| = ', NR)
    
    writer.write(X, R, NR)

    X , Y = inv(A) # нахождение обратной матрицы и 
    print('inverse:\n',X)
    for i in range(len(Y)):
        print(f'y{i} : {Y[i]}')
