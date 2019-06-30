#  Overall time complexity is O(n)


def non_divisible_subset_len(iterable, key):
    """
     Non-divisible subset length is the size of maximal subset of the iterable where
     sum of any two numbers in the subset is not evenly divisible by key
    :param iterable: The iterable should be of type list or tuple containing numbers
    :param key: key should be a number
    :return: Returns the length of the non-divisible subset of the iterable for given key
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
        raise ValueError("Doublet sum should be a number")

    # List to store all the remainders
    rem = []
    for num in iterable:  # storing all the remainders
        rem.append(num % key)

    tot = 0

    # If there is 0 in remainder list, we consider all zeros as 1
    if 0 in rem:
        tot += 1

    end = key // 2  # Half of the key

    if key % 2 == 0:  # If key is even
        if end in rem:
            tot += 1
    else:  # If key is odd
        end += 1

    for i in range(1, end):
        tot += max(rem.count(i), rem.count(key - i))

    return tot
