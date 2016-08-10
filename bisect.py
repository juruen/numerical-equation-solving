import math

PRECISION = 1E-10

def is_zero(a):
    return math.fabs(a) < PRECISION and math.fabs(a) > 0

def different_sign(a, b):
    return (a * b) < 0

def bisect(fn, a, b):
    """ Find a zero in the given function (fn) and two intervals a, b
        where fn(a) * fn(b) < 0, i.e: have distinct sign
    """
    if not different_sign(fn(a), fn(b)):
        raise ValueError("given interval doesn't change sign")

    while True:
        c = (a + b) / 2.0

        fc = fn(c)

        if is_zero(fc):
            return c

        if different_sign(fn(a), fc):
            b = c
        else:
            a = c


print bisect(lambda x: math.cos(x) - math.sin(x) + 0.4, 0, math.pi)
print bisect(lambda x: x*math.exp(x) - 1, 0, 1)
