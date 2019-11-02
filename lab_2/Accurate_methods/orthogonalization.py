from math import sqrt
import numpy as np
import numpy.linalg




def orthogonalization(A):

    def count_r(i, a, t, r):

        def count_t(i_r, i_a, a, r, t):
            s = 0
            q = 0
            for i in range(len(a)):
                s = s + a[i][i_a] * r[i][i_r]
                q = q + r[i][i_r]**2
            
            t[i_r, i_a] = s/q
            return t

        if i == 0:
            return a[:, 0]
        else:
            s = np.zeros((1 ,len(a)))
        for k in range(i):
            t = count_t(k, i, a, r, t)
            s += t[k][i] * r[:,k]
        return (a[:,i] - s)

    size_A = len(A)
    a = np.array(A)
    r = np.zeros((size_A, size_A))
    t = np.eye(size_A)

    #получаем R и T
    for i in range(len(a)):
        r[:, i] = count_r(i, a, t, r)

    return r, t


def Solve(A, b):
    size_A = len(A)
    A = np.array(A)
    b = np.array(b)
    R, T = orthogonalization(A)


    # R_tr = R.transpose()
    # D = R_tr.dot(R)
    # D_inv = numpy.linalg.inv(D)

    D = np.zeros((size_A, size_A)) #
    D_inv = np.zeros((size_A, size_A))

    for i in range(size_A):
        for k in range(size_A):
            D[i, i] += R[k, i] * R[k, i] # D = R'*R
        D_inv[i, i] = 1/D[i, i] #D(-1)Обратная

 
    R_tr = R.transpose()
    Beta = R_tr.dot(b) #Beta = R'b
    
    Y = D_inv.dot(Beta) #y = D(-1)*Beta (4.42 Мицель)
    
    X = np.zeros(Y.shape, dtype="float64")
    for i in range(size_A-1, -1, -1): #for(i = n-1; i > -1; i--)
        sum = 0.
        for j in range(size_A-1, i, -1): #for (j = n-1; j > i; j--)
            sum += X[j] * T[i,j]
        X[i] = (Y[i] - sum) / T[i,i]
    
    #print(f'X: {X}')
    R_Nev = A.dot(X) - b #Вектор невязки

    NR_r = R_Nev.max()

    NR_e = 0.0
    for e in np.nditer(R_Nev):
        NR_e += e**2
    NR_e = sqrt(NR_e)

    return X, R_Nev, NR_r, NR_e



def inverse(A) -> np.ndarray:
    '''
    Нахождение обратной матрицы A мотодом ортаганализации
    '''
    size_A = A.shape[0]
    # R = [None] * size_A
    # T = [None] * size_A
    a = [None] * size_A
    res = np.zeros([size_A, size_A])

    for i in range(size_A):
        a[i] = np.array([1. if j == i else 0.  for j in range(size_A) ])
        res[i], _, _, _  = Solve(A,a[i])  
        #res[i], R[i], T[i], _, _, _  = Solve(A,a[i])  
    # for i in range(len(R)):
    #     print(f'R{i}:\n{R[i]}')
    #     print(f'T{i}:\n{T[i]}')
    res = res.transpose()
    
    R_Nev = A.dot(res) - np.eye(A.shape[0])
    # print(f'A-1:\n{res}')
    return res, R_Nev




    
    





    
# def ort(A, R, T):
#     n = len(A)
#     s1 = s2 = 0.0
#     c = 1
#     for i in range(n):
#         if i > 0:
#             R = get_r_mat(A, R, T, i) 
        
#         for j in range(c, n):
#             s1 = scalar(A, R, j, i) 
#             s2 = scalar(R, R , i, i)
#             T[i, j] = s1/s2
#         c += 1

# def scalar(A, B, col1, col2):
#     n = len(A)
#     q = 0.0
#     for i in range(n):
#         q = q + (A[i, col1] * B[i, col2])
#     return q
    


# def get_r_mat(A, R, T, col):
#     n = len(A)
#     for i in range(n):
#         for j in range(col):
#             R[i, col] += T[j, col] * R[i, i]
#             R[i, col] = A[i, col] - R[i, col]
#     return R







