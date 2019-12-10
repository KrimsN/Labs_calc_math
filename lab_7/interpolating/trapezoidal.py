
def trapezoidal_dyn(f, a, b, n = 100):
	""" 
	Вычисляет приближенное значение интеграла с помощью формулы трапеций
	f - подынтегральная функция
	a, b - пределы интегрирования
	n - количество частичных отрезков
	"""
	h = float(b - a)/n
	result = 0.5*(f(a) + f(b))
	for i in range(1, n):
		result += f(a + i*h)
	result *= h
	return result


def trapezoidal_noneq(Y, H, n):
    double = Y[0]*H[0] + Y[n]*H[n-1] + sum(Y[i]*(H[i-1]+H[i]) for i in range(1, n))
    return 0.5*double


def trapezoidal_eq(Y, h, n):
    y = Y[0] + Y[n-1] + 2 * sum(Y[i] for i in range(n))
    return 0.5 * h * y