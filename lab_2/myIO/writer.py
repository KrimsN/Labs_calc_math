from typing import TextIO
import numpy as np

def write_mat(fp, m, prec=9):
    np.savetxt(fp, m, fmt='%0.{}e'.format(prec))

def write(output_file: TextIO, x=None, r=None, nr=None, X=None, e=None, ne=None, U=None, L=None):
    output_file.write('L :\n')
    write_mat(output_file, L)
    output_file.write('U :\n')
    write_mat(output_file, U)
    if x:
        output_file.write('x* = ' + str(x) + '\n')
        output_file.write('e = ' + str(r) + '\n')
        output_file.write('||r|| = ' + str(nr) + '\n')