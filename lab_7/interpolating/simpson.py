def sum1(a,n,f,xi):
    s = 0
    for i in range(a,n+1):
        s += f(xi[2*i-1])
    return s

def sum2(a,n,f,xi):
    s = 0
    for i in range(a,n+1):
        s += f(xi[2*i])
    return s

def simpson(f,a,b,n = 100):
    """ 
	Вычисляет приближенное значение интеграла с помощью формулы Симпсона
	f - подынтегральная функция
	a, b - пределы интегрирования
	n - количество частичных отрезков
	"""
    if n % 2 != 0:
        raise ValueError('Simpson: n is odd')
    h = (b - a) / (2 * n)
    xi = []

    for i in range(2*n+1):
        xi.append(a + i * h)

    sim = (h / 3) * ( f(xi[0]) + 4 * sum1(1,n,f,xi) + 2 * sum2(1,n-1,f,xi) + f(xi[2*n]))
    
    return sim

def simpson_noneq(Y, H, n):
    def single(Y, H, i):
        c = (H[2*i+1] + H[2*i]) / (6 * H[2*i+1] * H[2*i])
        h = [H[2*i+1] * (2*H[2*i] - H[2*i+1]),
             (H[2*i+1] + H[2*i]) ** 2,
             H[2*i] * (2*H[2*i+1] - H[2*i])]
        return c * sum(Y[2*i+j] * h[j] for j in range(3))
    if n % 2 != 0:
        raise ValueError('Simpson: n is odd')
    return sum(single(Y, H, i) for i in range(int(n/2)))