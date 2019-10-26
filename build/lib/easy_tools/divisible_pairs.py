
# Time Complexity is O(n)


def divisible_pairs(iterable, key):
    """
        Divisible-pairs gives the total number of divisible pairs in which
        the sum of the numbers from a pair is divisible by the given key
    :param iterable: The iterable should be of type list or tuple containing numbers
    :param key: key should be a number
    :return: Returns the total number of divisible pairs whose sum is divisible by given key

    Eg: divisible_pairs([1, 0, 0, 2, 5, 3],3) returns 5
        Here divisible pairs are {(0, 0), (0, 3), (0, 3), (1, 2}, (1, 5)}
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

    # To check whether the given key is a number or not
    if not isinstance(key, int):
        raise ValueError("Key should be a number")

    # Dictionary to store all the remainders and their number of occurrences
    rem = {}
    for num in iterable:
        remainder = num % key
        if remainder in rem.keys():
            rem[remainder] += 1
        else:
            rem[remainder] = 1

    pairs = 0

    # selecting two numbers out of n numbers is n C 2 ways i.e. (n(n-1))/2

    if 0 in rem.keys():  # since 0 is divisible by key
        pairs += (rem[0] * (rem[0] - 1)) // 2

    end = key // 2

    if key % 2 == 0:
        if end in rem.keys():  # since sum of two ends is equal to key
            pairs += (rem[end] * (rem[end] - 1)) // 2
    else:
        end += 1

    for i in range(1, end):
        # noinspection PyBroadException
        try:
            pairs += rem[i] * rem[key - i]
        except Exception:
            pass

    return pairs
