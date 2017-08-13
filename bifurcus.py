from functions import get_ricker_function, get_ricker_derivative
from utils import get_sequence
from math import pow, sqrt
from calculus import get_a, get_root


def get_range(start, end, delta):
    range_res = []
    curr = start
    while curr < end:
        range_res.append(curr)
        curr += delta
    return range_res


def get_start_point(r):  # подбор начальной точки на основе чисто эмпирического опыта
    if r > 0.35:
        return 2
    return 11


def get_bif(parameter_range, offset, count, start_point_function, epsilon, end_if_ext, stoch_offset=0):
    xs = []
    ys = []
    for parameter in parameter_range:
        start = start_point_function(parameter)
        func = get_ricker_function(parameter)
        sequence = get_sequence(start, func, offset, end_if_ext, 0.0)
        sequence = get_sequence(sequence[-1], func, stoch_offset, end_if_ext, epsilon)
        if not len(sequence) < stoch_offset:
            sequence = get_sequence(sequence[-1], func, count, end_if_ext, epsilon)
            if len(sequence) < count:
                sequence = []
        else:
            sequence = []
        for value in sequence:
            xs.append(parameter)
            ys.append(value)
    return xs, ys


def get_boundaries_for_range(parameter_range, epsilon, erf_value):
    xs = []
    ys = []
    for r in parameter_range:
        func = lambda x: get_ricker_function(r)(x) - x
        root = get_root(1.001, 100, func)  # хз, пока за рамки не выходит
        x_min, x_max = get_boundaries_for_equilibrium(root, get_ricker_derivative(r), erf_value, epsilon)
        xs.append(r)
        xs.append(r)
        ys.append(x_min)
        ys.append(x_max)
    return xs, ys


def get_boundaries_for_equilibrium(equilibrium, function, erf_value, epsilon):
    w = 1 / (1 - pow(function(equilibrium), 2))
    delta = erf_value * epsilon * sqrt(2 * w)
    return equilibrium - delta, equilibrium + delta


def get_cycle2_points(parameter_range):

    xs = []
    ys = []

    for r in parameter_range:
        cycle1, cycle2 = get_cycle2_points(r)
        xs.append(r)
        xs.append(r)
        ys.append(cycle1)
        ys.append(cycle2)

    return xs, ys


def w(a1, a2):
    return (1 + pow(a2, 2)) / (1 - pow(a1 * a2, 2))


def get_cycle_boundaries(c1, c2, r, erf_value, epsilon):
    a1, a2 = get_a(c1, c2, r)
    w1 = w(a1, a2)
    w2 = w(a2, a1)
    delta1 = erf_value * epsilon * sqrt(2 * w1)
    delta2 = erf_value * epsilon * sqrt(2 * w2)
    return c1 - delta1, c1 + delta1, c2 - delta2, c2 + delta2
