from bifurcus import get_bif, get_range, get_start_point, get_boundaries_for_range, get_cycle_boundaries
from utils import write_to_files, get_ladder, get_function_points, get_noise
from functions import get_ricker_function, get_ricker_composition, get_ricker_derivative
from calculus import get_cycle2_points, get_root


def f_main():  # just функция с лестницей Ламерея
    r = 2
    x_start = 1.2
    count = 100
    start = 0
    end = 2
    delta = 0.0001

    func = get_ricker_function(r)
    #func = get_ricker_composition(r)

    xl, yl = get_ladder(x_start, func, count)
    xl = xl[1:]
    yl = yl[1:]

    xpath = 'files/xlad.txt'
    ypath = 'files/ylad.txt'

    write_to_files(xl, yl, xpath, ypath)

    x, y = get_function_points(get_range(start, end, delta), func)

    xpath = 'files/fx.txt'
    ypath = 'files/fy.txt'

    write_to_files(x, y, xpath, ypath)


def extinction_cycle_main():  # только для генерации точек для костыльной картинки, принт границ интервада
    epsilon = 3
    r = 0.125
    curr = 10

    f = get_ricker_function(r)

    values = []

    while True:
        curr = f(curr) + get_noise(epsilon)
        values.append(curr)
        if curr <= 0:
            break

    indexes = [i for i in range(1, len(values) + 1)]

    xpath = 'files/pointst.txt'
    ypath = 'files/pointsv.txt'

    write_to_files(indexes, values, xpath, ypath)

    erf_value = 2.33
    c1, c2 = get_cycle2_points(r)
    ys = get_cycle_boundaries(c1, c2, r, erf_value, epsilon)
    print(ys)


def cycle2_main():  # зона 2-цикла: точки шумной биф диаграммы и доверительные интервалы
    delta = 0.00005
    start = 0.12
    end = 0.1788
    offset = 10000
    count = 1000
    stoch_offset = 1000
    epsilon = 0.5

    erf_value = 2.33

    rs = get_range(start, end, delta)

    xc, yc = get_bif(rs, offset, count, get_start_point, epsilon, True, stoch_offset)

    xcpath = 'files/cx.txt'
    ycpath = 'files/cy.txt'

    write_to_files(xc, yc, xcpath, ycpath)

    xbc = []
    ybc = []

    for r in rs:
        c1, c2 = get_cycle2_points(r)
        ys = get_cycle_boundaries(c1, c2, r, erf_value, epsilon)
        for y in ys:
            xbc.append(r)
            ybc.append(y)

    xbcpath = 'files/cbx.txt'
    ybcpath = 'files/cby.txt'

    write_to_files(xbc, ybc, xbcpath, ybcpath)


def bif_point_proof_main():  # уточнение первой точки бифуркации
    delta = 0.00001
    start = 0.177 + delta
    end = 0.179

    rs = get_range(start, end, delta)

    roots = []

    rs = [0.1787]

    precision = 0.0001

    for r in rs:
        f = get_ricker_function(r)
        der = get_ricker_derivative(r)
        equilibrium = get_root(1.01, 100, lambda x: f(x) - x, 0.000001)
        print(r)
        print(equilibrium)
        print(der(equilibrium))
        roots.append(equilibrium)
        # if -1 + precision < der(equilibrium) < 1 - precision:
        #     print(der(equilibrium))
        #     print(r)
        #     return


def bif_main():  # главная бифуркационная
    delta = 0.0001
    start = 0.2 + delta
    end = 0.5
    offset = 1000
    count = 300
    epsilon = 1.0

    rs = get_range(start, end, delta)

    x_stoch, y_stoch = get_bif(rs, offset, count, get_start_point, epsilon, True, 1000)

    xpath = 'files/bifx.txt'
    ypath = 'files/bify.txt'

    write_to_files(x_stoch, y_stoch, xpath, ypath)

    erf_value = 1.83

    x_b, y_b = get_boundaries_for_range(rs, epsilon, erf_value)

    xbpath = 'files/boundx.txt'
    ybpath = 'files/boundy.txt'

    write_to_files(x_b, y_b, xbpath, ybpath)


if __name__ == '__main__':
    #bif_main()
    #f_main()
    #cycle2_main()
    #stable_main()
    extinction_cycle_main()
