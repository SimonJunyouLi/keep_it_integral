def edge(u, v):
    if u < v:
        return (u, v)
    return (v, u)

def is_integral(x):
    return abs(x - 1) < 1e-5 or abs(x - 0) < 1e-5