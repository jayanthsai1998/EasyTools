# Time complexity is O(n)


def largest_number(iterable):
    """
     Largest_number is defined as the largest number formed by arranging the elements of the iterable
    :param iterable: It is of type list or tuple accepting only non-negative integers
    :return: The largest number possible from the given iterable
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

    # To check whether all the elements are non-negative integers
    for item in iterable:
        if item < 0:
            raise ValueError("Negative values not allowed")

    # Finding number of digits in the larger number
    lar_size = len(str(max(iterable))) + 1

    # Iterable for storing the numbers in the string format
    str_iterable = []

    for i in range(len(iterable)):
        str_iterable.append(((str(iterable[i]) * lar_size)[:lar_size], i))

    str_iterable.sort(reverse=True)

    # resultant number for storing the larger number from the iterable
    result = ""

    for item in str_iterable:
        result += str(iterable[item[1]])

    return int(result)
