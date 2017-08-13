from functions import get_ricker_function, get_ricker_composition, get_ricker_derivative


def get_root(start, end, function, precision=0.00001):
    if function(start) > function(end):
        func = lambda x: - function(x)
    else:
        func = function
    middle = (start + end) / 2
    while not - precision < func(middle) < precision:
        if func(middle) > 0:
            end = middle
        else:
            start = middle
        middle = (start + end) / 2
    return middle


def get_cycle2_points(r):
    f_start = 1.001
    f_end = 100
    f = lambda x: get_ricker_function(r)(x) - x
    f2 = lambda x: get_ricker_composition(r)(x) - x
    root = get_root(f_start, f_end, f)
    root_cycle_first = get_root(f_start, root - 0.001, f2)
    root_cycle_second = get_root(root + 0.001, f_end, f2)
    return root_cycle_first, root_cycle_second


def get_a(c1, c2, r):
    f = get_ricker_derivative(r)
    return f(c1), f(c2)
