
def left_rect(f, a, b, step):
    res = 0
    for x in range(a, b, step):
        res += f(x) * step
    return res



def right_rect(f, a, b, step):
    res = 0
    for x in range(b, a, -step):
        res += f(x) * step
    return res