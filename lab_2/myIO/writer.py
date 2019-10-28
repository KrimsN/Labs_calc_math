from typing import TextIO
import numpy as np

def write_mat(fp, m, string, prec=4, ty='e'):
    fp.write('\n' + string + ':\n')
    np.savetxt(fp, m, fmt='% {}.{}{}'.format(prec + 7, prec,ty))

def check(Obj):
    return not isinstance(Obj, type(None))

def write(f_out: TextIO, PLU=None, SLE=None, INV=None, DET=None):

#    if not isinstance(x, type(None)):
#        f_out.write('x* = ' + str(x) + '\n')
#        f_out.write('e = ' + str(r) + '\n')
#        f_out.write('||r|| = ' + str(nr) + '\n')
#
#    if not isinstance(X, type(None)):
#        print('ok')
#        np.savetxt(f_out, X)



    '''Если были переданы параметры L и U, то записываем их в файл'''
    if check(PLU):
        f_out.write('---------------P - L - U ----------------\n')

        write_mat(f_out, PLU['P'], 'P', prec=0,ty='f')
    
        write_mat(f_out, PLU['L'], 'L', ty='f')

        write_mat(f_out, PLU['U'], 'U', ty='f')

        f_out.write('\n-----------------------------------------\n')   

    '''Если были переданы параметры то записываем их в файл'''
    if check(SLE):
        f_out.write('-----------------Solve SLE---------------\n')

        write_mat(f_out, SLE['x'], 'x*')

        write_mat(f_out, SLE['y'], 'y')

        write_mat(f_out, SLE['e'], 'eps')

        f_out.write('\n||r|| : ' + str(SLE['NR']))

        f_out.write('\n-----------------------------------------\n')

    if check(INV):
        f_out.write('--------------------INV------------------\n')
        write_mat(f_out, INV['inv'], 'X')

        write_mat(f_out, INV['Norm'], 'Norm', prec=9)

        for i in range(len(INV['Y'])):
            write_mat(f_out, INV['Y'][i], 'Y' + str(i))
        f_out.write('-----------------------------------------\n')

    if check(DET):
        f_out.write('--------------------DET------------------\n')
        f_out.write('det: ' + str(DET))
        f_out.write('\n-----------------------------------------\n')