import numpy as np
import scipy.linalg
from pprint import pprint

def PLU_dec(A) -> (np.ndarray, np.ndarray, np.ndarray):
    """
    PLU-декомпозиция квадратной матрицы 
    """
    n = len(A)
    A = np.asarray(A,dtype=np.float64)
    L = np.asarray(np.identity(n))
    U = np.copy(A)
    P = np.identity(n)

    permutation = abs(U[:,0]).argsort()[::-1]
    U=U[permutation]
    P=P[permutation]

    for k in range(n):                          #for each column of A in Ab

        #Forward Elimination - Subtracting rows
        for j in range(k+1,n):                      #for each row under the diagonal of the kth column
            q = float(U[j][k]) / U[k][k]              #calculate the ratio to the value in the main diagonal

            L[j][k] = q

            for m in range(k, n):                     #for each each column in a Row j
                # Ab[j][m] -=  q * Ab[k][m]                   #calculate Rj - q*Rk.  This will result in all zeros under the main diagonal
                if m<len(U):
                    U[j][m] -= q * U[k][m]
    #x = np.zeros(n)
    
    U = np.triu(U)
    #L, U, P = (np.asmatrix(L), np.asmatrix(U),np.asmatrix(P))
    return P, L, U


def Solve_SLE(A: np.ndarray, b: np.ndarray) -> (np.ndarray, np.ndarray, np.ndarray, float) :
    '''
    Решение СЛАУ методом PLU-декомпозиции
    '''
    P,L,U = PLU_dec(A)

    #Ly = Pb
    Pb = P.dot(b)
    Y = np.zeros(Pb.shape)
    #print('Pb:\t', Pb)

    for i in range(len(Pb)):
        sum = 0.
        for j in range(i):
            sum += Y[j] * L[i][j]
        Y[i] = Pb[i] - sum

    #print('Y:\t',Y)

    #Ux = Y
    X = np.zeros(Y.shape, dtype="float64")
    for i in range(len(Y)-1, -1, -1):
        sum = 0.
        for j in range(len(Y)-1, i, -1):
            sum += X[j] * U[i,j]
        X[i] = (Y[i] - sum) / U[i,i]

    X = X.transpose()
    #print('X:\t', X)
    R = A.dot(X) - b #Вектор невязки
    #print('r:\t',R)
    NR_r = R.max()
    return X, Y, R, NR_r

def det_PLU(A) -> float:
    '''
    Нахождение детерменанта (определителя) методом PLU-декомпозиции
    '''
    
    def P_count(P: np.ndarray):
        '''
        Посчёт количества перестановок, дя верного определения знака определителя
        '''
        p_l = np.array([-1. for i in range(len(P))])
        for i in range(len(P)):
            for j in range(len(P)):
                if P[i,j] == 1: p_l[i] = j
        
        count = 0

        for i in range(len(p_l)):
            for j in range(i+1, len(p_l)):
                if p_l[i] > p_l[j]: count += 1
                    
        return (-1) ** count
    
    P, L, U = PLU_dec(A)
    Det_A = 1
    for i in range(len(A)):
        Det_A *= U[i,i]
    Det_A *= P_count(P)
    return Det_A


def inverse(A) -> np.ndarray:
    '''
    Нахождение обратной матрицы A мотодом PLU-декомпозиции
    '''
    X__ = A.shape[0]

    a =  y = [None] * X__
    res = np.zeros([X__, X__])

    for i in range(X__):
        a[i] = np.array([1. if j == i else 0.  for j in range(X__) ])
        res[i], y[i], _, _  = Solve_SLE(A,a[i]) #TODO 
         
    return res.transpose(), y


if __name__ == "__main__":

    myA = [[20.9, 1.2, 2.1, 0.9], [1.2, 21.2, 1.5, 2.5],[2.1, 1.5, 19.8, 1.3], [0.9, 2.5, 1.3, 32.1]]
    myB = [21.7, 27.46, 28.76, 49.72]
    myA = [
    [ 1.0, -2.0,  3.0,  -4.0],
    [ 3.0,  3.0, -5.0,  -1.0],
    [ 3.0,  0.0,  3.0, -10.0],
    [-2.0,  1.0,  2.0,  -3.0]
    ]
    
    myB = [
        2.0,
        -3.0,
        8.0,
        5.0
    ]


    b = np.array(myB)
    A = np.array(myA)
    print('\n\ndet_PLU: ',det_PLU(A))
    #print('\n\ndet: ',scipy.linalg.det(A))

    print('\nMy\n')
    X, Y, R, NR = Solve_SLE(A, b)
    print('x* = ', X)
    print('y = ', Y)
    print('r = ', R)
    print('||r|| = ', NR)

    
    X , Y = inverse(A)
    print('inverse:\n',X)
    for y in Y:
        print(f'yi : {y}')
