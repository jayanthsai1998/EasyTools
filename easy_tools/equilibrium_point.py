# Time complexity is O(2n) i.e O(n)


def equilibrium_point(iterable):  # returns index of equilibrium point
    """
    Equilibrium point is the index in the iterable in which the sum of elements on left hand side and right side of the index are equal.
    :param iterable: The iterable should be of type list or tuple
    :return: It returns the index position of the equilibrium point in the iterable, and if no such index is present or list is empty it returns -1
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
