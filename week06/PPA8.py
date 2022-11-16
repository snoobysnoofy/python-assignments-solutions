def factors(n):
    factors = set()
    for i in range(1, n+1):
        if n % i == 0:
            factors.add(i)
    return factors


def common_factors(a, b):
    cf = set()
    fa = factors(a)
    fb = factors(b)
    return fa.intersection(fb)


def factors_upto(n):
    d = {}
    for i in range(1, n+1):
        d[i] = factors(i)
    return d
    