# Time complexity is O(n)


def leaders_to_left(iterable):
    """
     Leaders-to-left in the iterable is defined as if an element in the iterable
     is greater than all other elements to it's left side
    :param iterable: It should be of either list or tuple types containing numbers
    :return: list of tuples containing leader element and its index
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

    # List to store the left leaders
    leaders_list = []

    if len(iterable) > 0:
        leaders_list.append((iterable[0], 0))

    for i in range(1, len(iterable)):
        if iterable[i] >= leaders_list[-1][0]:
            leaders_list.append((iterable[i], i))

    return leaders_list
