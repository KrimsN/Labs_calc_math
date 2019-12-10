
import numpy as np
import argparse

from class_function import Function

from interpolating.rectangle_rule import left_rect, right_rect
from interpolating.trapezoidal import trapezoidal
from interpolating.simpson import simpson

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
        
        if args.grid_type == 'dyn':
            reader.read()




if __name__ == "__main__":
    main()