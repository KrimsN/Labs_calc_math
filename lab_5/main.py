import numpy as np

from math import sqrt
import argparse 

from myIO import reader, writer
from newton import NewtonPolynomialN, NewtonPolynomialE, Function

def averange(arr):
    arr = arr or [0]
    return sum(arr) / len(arr)

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
                a, b, Y, test_l, anal_func = reader.read(f_in, args.grid_type)
                Poly = NewtonPolynomialE(a, b, Y)
                print(f'a={a}\t b={b}')
            else: 
                X, Y, test_l, anal_func = reader.read(f_in, args.grid_type)
                Poly = NewtonPolynomialN(X, Y)
                print(f'X: {X}')

        print(f'Y: {Y}\n')
        print(f'x_res: {test_l}')
        print(anal_func)
        
        if anal_func:
            anal_func = Function(anal_func)


        with open(args.output, 'w') as f_out:
            f_l = []
            eps = []
            for t in test_l:
                f_l.append( Poly(t, args.deriv_order) ) 
                if anal_func:
                    eps.append( f_l[-1] - anal_func(t, args.deriv_order) )
            
            aver = averange(eps)
            sigma = sqrt( sum([(x_i - aver) ** 2 for x_i in eps]) / len(eps))

            writer.write(f_out, test_l, f_l, sigma)
            print(f_l)
            print(sigma)





    except Exception as e:
        print(e)




if __name__ == "__main__":
    main()