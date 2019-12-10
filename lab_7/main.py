
import numpy as np
import argparse

from class_function import Function

from interpolating.rectangle_rule import *
from interpolating.trapezoidal import *
from interpolating.simpson import *

from myIO import reader, writer




#test func
from scipy.integrate import quad
#

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-g', '--grid_type', action="store", default='dyn', choices=['dyn', 'eq', 'noneq'], help="Тип сетки: dyn - динамическая; eq - равномерная; noneq - неравномерная.")
    parser.add_argument('-l', '--left_rect', action="store_true", help="Найти методом левых прямоугольников")
    parser.add_argument('-r', '--right_rect', action="store_true", help="Найти методом правых прямоугольников")
    parser.add_argument('-t', '--trapezoidal', action="store_true", help="Найти методом трапеций")
    parser.add_argument('-s', '--simpson', action="store_true", help="Найти методом Симпсона")
    parser.add_argument('-in', '--input', action="store", default='input.txt')
    parser.add_argument('-o', '--output', action="store", default='output.txt')
    args = parser.parse_args()
    try:
        
        with open(args.input) as f_in:
            if args.grid_type == 'dyn':
                n, a, b, func = reader.read(f_in, args.grid_type)
                print(f'dyn:\n n: {n}\t(a, b): ({a}, {b})\t f: {func}\n')
            elif args.grid_type == 'eq':
                n, h, Y = reader.read(f_in, args.grid_type)
                print(f'eq:\n n: {n}\th: {h}\t\n Y: {Y}\n')
            elif args.grid_type == 'noneq':
                n, X, Y = reader.read(f_in, args.grid_type)
                print(f'eq:\n n: {n}\t\nX: {X}\t\n Y: {Y}\n')



        if args.grid_type == 'dyn':
            if args.left_rect:
                left_res = left_rect_dyn(func, a, b, n)
            if args.right_rect:
                right_res = right_rect_dyn(func, a, b, n)
            if args.trapezoidal:
                trap_res = trapezoidal_dyn(func, a, b, n)
            if args.simpson:
                simp_res = simpson_dyn(func, a, b, n)

        elif args.grid_type == 'eq':
            if args.left_rect:
                left_res = left_rect_eq(Y, h, n)
            if args.right_rect:
                right_res = right_rect_eq(Y, h, n)
            if args.trapezoidal:
                trap_res = trapezoidal_eq(Y, h, n)
            if args.simpson:
                simp_res = simpson_eq(Y, h, n)

        elif args.grid_type == 'noneq':
            if args.left_rect:
                left_res = left_rect_noneq(Y, X, n)
            if args.right_rect:
                right_res = right_rect_noneq(Y, X, n)
            if args.trapezoidal:
                trap_res = trapezoidal_noneq(Y, X, n)
            if args.simpson:
                simp_res = simpson_noneq(Y, X, n)

        print(f'left: {left_res}')
        print(f'right: {right_res}')
        # print(f'delta: {(left_res + right_res)/2}')
        print(f'trap: {trap_res}')
        print(f'simp: {simp_res}')

    finally:
        pass
        

                
        
        




if __name__ == "__main__":
    main()