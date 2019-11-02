import math
import numpy as np
import numpy.linalg

def fill(A):
    size = len(A)
    tmp = [[3, 8, -4], [1, 5, 2], [6, -4, 1]]
    for i in range(size):
        for j in range(size):
            A[i, j] = tmp[i][j]
    return A

def count_t(i_r, i_a, a, r, t):
  s = 0
  q = 0
  for i in range(len(a[0])):
    s = s + a[i][i_a] * r[i][i_r]
    q = q + r[i][i_r]**2
  
  t[i_r, i_a] = s/q

def count_r(i, a, t, r):
  if i == 0:
    return a[:, 0]
  else:
    s = np.zeros((1 ,len(a[0])))
   
    
    for k in range(i):
      
      count_t(k, i, a, r, t)
      s += t[k][i] * r[:,k]
         
    return (a[:,i] - s)

def orthogonalization(A, b):
    size_A = len(A)
    b = np.array(b)
    a = np.array(A)
    r = np.zeros((size_A, size_A))
    t = np.eye(size_A)
    Ans = np.zeros((size_A, size_A))

    #получаем R и T
    for i in range(len(a[0])):
        r[:, i] = count_r(i, a, t, r)

    print(f'A:\n{a}\nR:\n{r}\nT:\n{t}')

    R_tr = r.transpose()

    D = R_tr.dot(r)
    

    D_inv = numpy.linalg.inv(D)
    
    Beta = R_tr.dot(b)
    
    
    Y = D_inv.dot(Beta)
    

    X = np.zeros(Y.shape, dtype="float64")
    for i in range(len(Y)-1, -1, -1):
        sum = 0.
        for j in range(len(Y)-1, i, -1):
            sum += X[j] * t[i,j]
        X[i] = (Y[i] - sum) / t[i,i]
    
    print(f'X: {X}')


def Solve(A,b):
    pass

def inverse(A) -> np.ndarray:
    '''
    Нахождение обратной матрицы A мотодом PLU-декомпозиции
    '''
    X__ = A.shape[0]

    a =  y = [None] * X__
    res = np.zeros([X__, X__])

    for i in range(X__):
        a[i] = np.array([1. if j == i else 0.  for j in range(X__) ])
        res[i], y[i], _, _, _  = Solve(A,a[i]) #TODO 
    res = res.transpose()
    
    R = A.dot(res) - np.identity(A.shape[0])
    print(f'A-1:\n{res}')
    return res, y, R




    
    





    
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







