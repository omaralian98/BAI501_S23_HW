import math


def get(depth, nodes, error=0.001):
    lower_bound = 1 + error
    upperbound = math.pow(nodes, float(1/depth))
    return _bi_section(lower_bound, upperbound, depth, nodes, error)


def _bi_section(a, b, depth, nodes, error):
    x = (a + b) / 2
    fx = (math.pow(x, depth + 1) - 1) / (x - 1)
    if abs(fx - (nodes + 1)) <= error:
        return x
    if fx > nodes + 1:
        return _bi_section(a, x, depth, nodes, error)
    else:
        return _bi_section(x, b, depth, nodes, error)
