from math import pow, exp


def f(x, r):
    return pow(x, 2) * exp(r * (1 - x))


def f_derivative(x, r):
    return (2 * x - r * pow(x, 2)) * exp(r * (1 - x))


def get_ricker_composition(r):
    func = get_ricker_function(r)
    return lambda x: func(func(x))


def get_ricker_function(r):
    return lambda x: f(x, r)


def get_ricker_derivative(r):
    return lambda x: f_derivative(x, r)
