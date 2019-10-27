import numpy as np
from typing import TextIO

def write(output_file: TextIO, x=None, r=None, nr=None, X=None, e=None, ne=None, U=None, L=None):
    output_file.write('x* = ' + str(x) + '\n')
    output_file.write('e = ' + str(r) + '\n')
    output_file.write('||r|| = ' + str(nr) + '\n')
