#  Overall time complexity is O(n)


def non_divisible_subset_len(iterable, key):
    """
     Non-divisible subset length is the size of maximal subset of the iterable where
     sum of any two numbers in the subset is not evenly divisible by key
    :param iterable: The iterable should be of type list or tuple containing numbers
    :param key: key should be a number
    :return: Returns the max length of the non-divisible subset of the iterable for given key

    Eg: non_divisible_subset_len([1, 0, 0, 2, 5, 3],3) returns 3
        Here maximal length subset is (0, 2, 5) or (2, 3, 5)
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

    max_subset_len = 0

    # If there is 0 in remainder list, we consider all zeros as single zero and added to the subset
    # since no other value can add up to zero in remainder list to divide with key
    if 0 in rem.keys():
        max_subset_len += 1

    end = key // 2  # Half of the key

    if key % 2 == 0:  # If key is even
        if end in rem.keys():  # All the set of elements which are half of the key can be considered as single
                                # and added to the subset because no other element can add upto it
                                # except the element itself to divide with the key
            max_subset_len += 1
    else:  # If key is odd
        end += 1

    for i in range(1, end):
        max_subset_len += max(rem[i], rem[key - i])

    return max_subset_len
