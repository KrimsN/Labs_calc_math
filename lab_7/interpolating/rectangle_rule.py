
def left_rect_dyn(f, a, b, n = 100):
    """ 
	Вычисляет приближенное значение интеграла методом левостороннеего прямоугольника
    f - подынтегральная функция
	a, b - пределы интегрирования
	n - количество частичных отрезков
	"""
    h = float(b-a)/n
    res = 0
    x = a
    
    for i in range(n):
        res += f(x) * h
        x += h
    return res



def right_rect_dyn(f, a, b, n = 100):
    """ 
	Вычисляет приближенное значение интеграла методом правостороннеего прямоугольника
    f - подынтегральная функция
	a, b - пределы интегрирования
	n - количество частичных отрезков
	"""
    h = float(b-a)/n
    res = 0
    x = b
    
    for i in range(n):
        res += f(x) * h
        x -= h
    return res


def left_rect_noneq(Y, H, n):
    return sum(Y[i] * H[i] for i in range(n))


def right_rect_noneq(Y, H, n):
    return sum(Y[i+1] * H[i] for i in range(n))


def left_rect_eq(Y, h, n):
    return h * sum(Y[i] for i in range(n))


def right_rect_eq(Y, h, n):
    return h * sum(Y[i] for i in range(1, n+1))