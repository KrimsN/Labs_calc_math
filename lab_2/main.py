import numpy as np
import scipy.linalg
import argparse 
#from pprint import pprint
#from IO import reader, writer
from Accurate_methods.LU_decomposition import Solve as Solve_LU, inverse as inv, determinant as det
import Iterative_methods.seidel as Sei

from myIO import reader, writer




if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('method', help='метод работы с матрицей', choices=['LU', 'Seidel'])
    parser.add_argument('-s', '--solve', help='Решить СЛАУ', action="store_true")
    parser.add_argument('-i', '--inverse', help='Найти обратную матрицу', action="store_true")
    parser.add_argument('-d', '--determinant', help='Найти определитель матрицы', action="store_true")
    parser.add_argument('-in', '--input', action="store", default='input.txt')
    parser.add_argument('-o', '--output', action="store", default='output.txt')
    args = parser.parse_args()

    in_f = open(args.input, 'w')

    
    if args.solve:
        A , b = reader.read(in_f, SLE=True)
    else:
        A = reader.read(in_f, SLE=False)
    

    if args.method == 'LU':
        if args.solve:
            X, Y, R, NR_r, NR_e = Solve_LU(A, b)
        if args.inverse:
            A_inv = inv(A)
        if args.determinant:
            A_det = det(A)



    elif args.method == 'Seidel':
        if args.solve:
            eps = 1e-1
            alpha, beta, NR_r = Sei.Solve(A, b, eps)
        if args.inverse or args.determinant:
            raise KeyError('У метода Зейделя не определены операции инвертирования и нахождение определителя.')
    else:
        print('EROOR')





    myA = [[20.9, 1.2, 2.1, 0.9], [1.2, 21.2, 1.5, 2.5],[2.1, 1.5, 19.8, 1.3], [0.9, 2.5, 1.3, 32.1]]
    myB = [21.7, 27.46, 28.76, 49.72]
    myA = [
    [ 1.0, -2.0,  3.0,  -4.0],
    [ 3.0,  3.0, -5.0,  -1.0],
    [ 3.0,  0.0,  3.0, -10.0],
    [-2.0,  1.0,  2.0,  -3.0]
    ]
    
    
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
    X, Y, R, NR, NR_e = Solve_LU(A, b) # X - вектор решения, Y - временный вектор, R - вектор невязка, NR - норма вектора невязки
    print('x* = ', X)
    print('y = ', Y)
    print('r = ', R)
    print(f'||r|| = {NR} or {NR_e}')
    writer.write(X, R, NR)

    X , Y, NR = inv(A) # нахождение обратной матрицы и 
    print('inverse:\n',X)
    print(f'Norm:\n{NR}')

    np.set_printoptions(precision=2, suppress=False)
    print(type(Y))
    for i in range(len(Y)):
        print(f'y{i} : {Y[i]}')

    in_f.close()

