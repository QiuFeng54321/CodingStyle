def sum_of_square(n):
    """Sums the square of all x from 1 to n inclusive and returns the result
    :param n: The upper bound of the summation
    :type n: int
    :raises ArithmeticError: n is less than 0
    :returns: The square sum from 1 to n inclusive
    :rtype: int
    """
    if n < 0:
        raise ArithmeticError("n should be greater than or equal to 0")
    return n * (n + 1) * (2 * n + 1) / 6
