import numpy as np

def write(x, r, nr, filename='output.txt'):
    file = open(filename, 'w')
    file.write('x* = ' + str(x) + '\n')
    file.write('e = ' + str(r) + '\n')
    file.write('||r|| = ' + str(nr) + '\n')
