import math

class Polynomial:
    def __init__(self, coef_list: list(str)):
        self.coefficients = coef_list
        self.evaluate = self.create_evaluation_function()
        self.degree = len(self.coefficients) - 1

    def __add__(self, poly: "Polynomial"):
        diff_len = len(self.coefficients) - len(poly.coefficients)
        if diff_len > 0:
            poly.coefficients += [0] * diff_len
        elif diff_len < 0:
            self.coefficients += [0] * -diff_len
        new_coefficients = [self.coefficients[i] + poly.coefficients[i]
                            for i in range(len(self.coefficients))]
        return Polynomial(new_coefficients)

    def __iadd__(self, poly: "Polynomial"):
        return self.__add__(poly)

    def __mul__(self, poly: "Polynomial"):
        # Scalar multiplication case
        if type(poly) == int or type(poly) == float:
            return Polynomial([poly * coef for coef in self.coefficients])
        # Polynomial multiplication case
        new_coefficients = [0] * (self.degree + poly.degree + 1)
        for i in range(len(self.coefficients)):
            for j in range(len(poly.coefficients)):
                new_coefficients[i + j] += self.coefficients[i] * \
                    poly.coefficients[j]
        return Polynomial(new_coefficients)

    def __imul__(self, poly: "Polynomial"):
        return self.__mul__(poly)

    def __repr__(self) -> str:
        representation = ""
        for i in range(len(self.coefficients) - 1, 0, -1):
            if self.coefficients[i] == 1:
                representation += f"x^{i} + "
            elif self.coefficients[i] != 0:
                representation += f"{self.coefficients[i]}x^{i} + "
        if self.coefficients[0] != 0:
            representation += f"{self.coefficients[0]}"
        else:
            representation = representation[:-3]
        return representation

    def __str__(self) -> str:
        return self.__repr__()

    def __call__(self, x: complex) -> complex:
        res = 0
        for (i, coefficient) in enumerate(self.coefficients):
            res += coefficient * math.pow(x, i)
        return res

    def map_to_int(self):
        new_coefficients = [round(coef) for coef in self.coefficients]
        return Polynomial(new_coefficients)

    def get_roots(self):
        # TODO
        pass

    def get_single_root(self):
        # TODO
        stable_point = 0

    def create_evaluation_function(self):
        return self.__call__
