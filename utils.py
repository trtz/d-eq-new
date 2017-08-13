from random import normalvariate


def get_noise(epsilon):
    return epsilon * normalvariate(0, 1)


def write_to_files(xs, ys, xpath, ypath):
    write_to_file(xs, xpath)
    write_to_file(ys, ypath)


def write_to_file(points, path):
    acc = ''
    for point in points:
        acc += str(point) + '\n'
    with open(path, 'w') as file:
        file.write(acc)


def get_ladder(start, function, count):
    x_lad = [start]
    y_lad = [0]
    sequence = get_sequence(start, function, count, False, 0)[1:]
    for value in sequence:
        x_lad.append(x_lad[-1])
        y_lad.append(value)
        x_lad.append(value)
        y_lad.append(value)
    return x_lad, y_lad


def get_sequence(start, function, count, end_if_extinction, epsilon):
    sequence = [start]
    curr = start
    for _ in range(count):
        curr = function(curr) + get_noise(epsilon)
        if end_if_extinction and curr <= 0:
            break
        sequence.append(curr)
    return sequence


def get_function_points(arg_range, func):
    return arg_range, list(map(func, arg_range))
