import numpy as np

import argparse 

from myIO import reader, writer
from newton import NewtonPolynomialN, NewtonPolynomialE


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('grid_type', help='тип ввода значений (сетка равномерная(un) или неравномерная(nonun))', choices=['un', 'nonun'])
    parser.add_argument('-d', '--deriv_order', action="store",type=int, default=0, help="порядок производной")
    parser.add_argument('-in', '--input', action="store", default='input.txt')
    parser.add_argument('-o', '--output', action="store", default='output.txt')
    args = parser.parse_args()


    try:

        if args.deriv_order < 0 or args.deriv_order > 2:
            raise Exception("-d must be greater than 0 and less than 2")


        with open(args.input, 'r') as f_in:
                
            if args.grid_type == 'un':
                a, b, Y, test_l= reader()
                Poly = NewtonPolynomialE(a, b, Y)
            else: 
                X, Y, test_l = reader()
                Poly = NewtonPolynomialN(X, Y)

        with open(args.output, 'w') as f_out:
            f_l = []
            for t in test_l:
                f_l.append( Poly(t, args.deriv_order) ) 
            print(f_l)





    except Exception as e:
        print(e)




if __name__ == "__main__":
    main()