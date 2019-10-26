# Time complexity is O(2n) i.e O(n)


def equilibrium_point(iterable):  # returns index of equilibrium point
    """
    Equilibrium point is the index in the iterable in which the sum of elements on the
    left hand side and the right side of that index are equal.
    :param iterable: The iterable should be of type list or tuple
    :return: It returns the index position of the equilibrium point in the iterable,
             and if no such index is present or list is empty it returns -1

        Eg: equilibrium_point([-9, 1, 5, 2, -6, 3, 0]) returns 3
            Here the sum of elements on either side of the index 3 is '-3'.
    """

    # To check whether the given iterable is list or tuple
    if type(iterable) == list or type(iterable) == tuple:
        pass
    else:
        raise TypeError("Iterable should be of either list or tuple")

    # To check whether all the given items in the iterable are numbers only
    for item in iterable:
        if not isinstance(item, int):
            raise ValueError("Only numbers are accepted in the iterable")

    total = sum(iterable)
    left_sum = 0
    for i in range(len(iterable)):
        total -= iterable[i]
        if total == left_sum:
            return i
        left_sum += iterable[i]
    return -1
