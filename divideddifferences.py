def divided_diffs(fn, xs):
    """ Compute divided differences recursiverly of a passed
        function (fn) over the points passed in xs
    """
    if not xs:
        raise ValueError("xs is empty")

    if len(xs) == 1:
        return fn(x)

    denominator = xs[-1] - xs[0]

    if denominator == 0:
        raise ValueError("two contigious points are equal")

    numerator = divided_diffs(fn, xs[1:]) - divided_diffs(fn, xn[:-1])

    return numerator / float(denominator)
