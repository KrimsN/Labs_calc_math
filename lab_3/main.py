import numpy as np
import argparse

from sys import stdin, stdout

from numpy.linalg import det
from numpy import eye

from danilevsky import get_danilevsky_mtx, get_lamda_list, get_S, get_frob_ver

from myIO import reader
from myIO.writer import write_mtx





def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--task_type', action="store", type=int, default=2, choices=[1, 2], help="Номер типа задачи. 1 - нахождение собсвенных чисел матрицы. 2 - нахождение собственных векторов.")
    parser.add_argument('-in', '--input', action="store", default='input.txt')
    parser.add_argument('-o', '--output', action="store", default='output.txt')
    args = parser.parse_args()

    try:
        with open(args.input, 'r') as f_in:
            A = reader.read(f_in)
            n = A.shape[0]

        eps = 1e-5

        P, B_l, B_inv_l = get_danilevsky_mtx(A)
        lambda_l = get_lamda_list(P)

        S = None

        with open(args.output, 'w') as f_out:
            # Записываем в файл матрицу Фрабениуса
            f_out.write('Frobenius matrix:\n')
            write_mtx(f_out, P)
            f_out.write('--\n')
            for lam in lambda_l:
                f_out.write(f'lam = {lam["r"]}\n--\n')

                if args.task_type == 1:
                    d = det(A - eye(n).dot(l['r']))
                    f_out.write(f'det(A-lam * E)={d}\n--\n')
                
                elif args.task_type == 2:
                    S = get_S(B_l) if S is None else S
                    y = get_frob_ver(lam['r'], n)
                    x = S.dot(y)
                    f_out.write('x:\n')
                    write_mtx(f_out, x)

                    f_out.write('--\neps:\n')
                    write_mtx(f_out, A.dot(x) - x.dot(lam['r']))
                
                f_out.write(f'--\nk={lam["k"]}\n\n--------\n')

    # except Exception as e:
    #     print(e)
    finally:
        pass






if __name__ == "__main__":
    main()