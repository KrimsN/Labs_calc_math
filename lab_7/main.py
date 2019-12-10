
import numpy as np
from class_function import Function
from interpolating.rectangle_rule import left_rect, right_rect
from interpolating.trapezoidal import trapezoidal
from interpolating.simpson import simpson_method
from myIO import reader, writer




#test func
from scipy.integrate import quad
#

def main():
    a = 1
    b = 2
    f_str = 'x^2'
    func = Function(f_str)

    res = left_rect(func, a, b)
    print('left: ', res)
    res = right_rect(func, a, b)
    print('right: ', res)
    res = trapezoidal(func, a, b)
    print('trap: ', res)

    simpson_method(func, a, b, 0.02)

    res, _ = quad(func, a, b)
    print('test: ', res)




if __name__ == "__main__":
    main()