from copy import copy


class PolynomialFunction:
    def __init__(self, coeffs):
        self.coeffs = list(coeffs)
        if len(self.coeffs) == 0:
            self.coeffs.append(0.0)

    @property
    def degree(self):
        return len(self.coeffs)-1

    def deriv(self):
        new_coeffs = copy(self.coeffs)
        for i in range(1, len(new_coeffs)):
            new_coeffs[i-1] = i * new_coeffs[i]
        new_coeffs.pop()
        if len(new_coeffs) == 0:
            new_coeffs.append(0.0)
        return PolynomialFunction(new_coeffs)

    def __getitem__(self, i):
        return self.coeffs[i]

    def __call__(self, x, deriv=0):
        f = self
        for i in range(deriv):
            f = f.deriv()
        res = sum((x**i * f[i]) for i in range(len(self.coeffs) - deriv))
        return res
