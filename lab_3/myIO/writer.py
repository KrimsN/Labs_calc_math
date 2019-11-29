import numpy as np
from typing import TextIO


def write_mtx(fp: TextIO, m, prec=9, type_o='f'):
    np.savetxt(fp, m, fmt=f'%0.{prec}{type_o}')
