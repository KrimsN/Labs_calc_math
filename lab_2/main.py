import numpy as np
import scipy.linalg
import argparse 
import os
#from pprint import pprint
#from IO import reader, writer
from Accurate_methods.LU_decomposition import Solve as Solve_LU, inverse as inv, determinant as det, PLU_decomposition as LU
import Iterative_methods.seidel as Sei

from myIO import reader, writer




if __name__ == "__main__":
    os.system('cls')
    parser = argparse.ArgumentParser()
    parser.add_argument('method', help='метод работы с матрицей', choices=['LU', 'Seidel'])
    parser.add_argument('-s', '--solve', help='Решить СЛАУ', action="store_true")
    parser.add_argument('-i', '--inverse', help='Найти обратную матрицу', action="store_true")
    parser.add_argument('-d', '--determinant', help='Найти определитель матрицы', action="store_true")
    parser.add_argument('-in', '--input', action="store", default='input.txt')
    parser.add_argument('-o', '--output', action="store", default='output.txt')
    args = parser.parse_args()

    
    with open(args.input, 'r') as f_in:
    
        if args.solve:
            A, b = reader.read(f_in, SLE=True)
            A, b = np.array(A), np.array(b)
            print('A:\n', A, 'b:\n', b)
        else:
            A , b = reader.read(f_in, SLE=False)
            A = np.array(A)
            print('A:\n', A)
        print('---------------------------------------')


    with open(args.output,'w') as f_out:
        
        if args.method == 'LU':
            P, L, U = LU(A)
            writer.write(f_out, {'P':P, 'L':L, 'U':U})
            if args.solve:
                print('--------------Solve SLE----------------')
                X, Y, R, NR_r, NR_e = Solve_LU(A, b)  # X - вектор решения, Y - временный вектор, R - вектор невязка, NR_r - норма вектора невязки, NR_e - евклиидова норма
                print('\nMy\n')
                print('x* = ', X)
                print('y = ', Y)
                print('r = ', R)
                print(f'||r|| = {NR_r} or {NR_e}')
                print('---------------------------------------')
                writer.write(f_out, SLE={'x':X, 'y':Y, 'e':R, 'NR':NR_e})



            if args.inverse:
                print('---------------inverse-----------------')
                A_inv, Y_list, R_inv = inv(A)
                print('inverse:\n', A_inv)
                print(f'Norm:\n{R_inv}')
                for i in range(len(Y_list)):
                    print(f'y{i} : {Y_list[i]}')
                print('---------------------------------------')

                writer.write(f_out, INV={'inv': A_inv, 'Norm':R_inv, 'Y':Y_list})
                
            if args.determinant:
                print('-------------determinant---------------')
                A_det = det(A)
                print('det_PLU: ', A_det)
                print('---------------------------------------')

                writer.write(f_out, DET=A_det)

        elif args.method == 'Seidel':
            if args.solve:
                eps = 1e-1
                alpha, beta, NR_r = Sei.Solve(A, b, eps)
            if args.inverse or args.determinant:
                raise KeyError('У метода Зейделя не определены операции инвертирования и нахождение определителя.')
        else:
            print('EROOR')




    '''
    myA = [[20.9, 1.2, 2.1, 0.9], [1.2, 21.2, 1.5, 2.5],[2.1, 1.5, 19.8, 1.3], [0.9, 2.5, 1.3, 32.1]]
    myB = [21.7, 27.46, 28.76, 49.72]
    myA = [
    [ 1.0, -2.0,  3.0,  -4.0],
    [ 3.0,  3.0, -5.0,  -1.0],
    [ 3.0,  0.0,  3.0, -10.0],
    [-2.0,  1.0,  2.0,  -3.0]
    ]
    '''
    

    f_in.close()

