
# Overall time complexity is O(n log n)

# Return True when sum of any three numbers from the iterable equals to given triplet_sum
# else returns False


def triplet_occurrence(iterable, triplet_sum):

    """
    A triplet is said to be present if any of the three numbers in the iterable is equal to given triplet_sum
    :param iterable: Iterable should be either of the types list or tuple of minimum length 3 with numbers
    :param triplet_sum: Triplet sum should be a number
    :return: True if triplet is present, else False
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

    # To check whether the given triplet_sum is a number
    if not isinstance(triplet_sum, int):
        raise ValueError("Triplet sum should be a number")

    # The length of the iterable should be of minimum length 3
    if len(iterable) < 3:
        raise Exception("Length of the given iterable should be of minimum length 3")

    # Iterable of any type is converted to list type to perform sort operation
    iterable = list(iterable)

    # First we sort the list which takes O(n log n) time complexity
    iterable.sort()

    # Initially considering first, second and last elements of iterable as the triplets
    low = 0
    mid = 1
    high = len(iterable) - 1

    current_sum = iterable[low] + iterable[mid] + iterable[high]

    # Dictionary for storing the previous sum values
    occur = dict()
    occur[iterable[low] + iterable[high]] = [iterable[low], iterable[high]]
    occur[iterable[mid] + iterable[high]] = [iterable[mid], iterable[high]]

    # Here a single element is accessed at most two times in the worst case which may be O(2n)
    # Hence the complexity for below loop is O(n)
    while mid < high:

        # If we got the current sum is equal to the triplet sum, we are returning True
        if current_sum == triplet_sum:
            return True

        # If the current sum is less than triplet sum
        elif current_sum < triplet_sum:

            # If mid is very next to low, we are incrementing the index of mid
            if mid - low == 1:
                mid += 1
                if triplet_sum - iterable[mid] in occur.keys():
                    return True
                occur[iterable[high] + iterable[mid]] = [iterable[mid], iterable[high]]
                occur[iterable[low] + iterable[mid]] = [iterable[low], iterable[mid]]
                current_sum += iterable[mid] - iterable[mid - 1]

            # If they are not adjacent we are incrementing the index of low
            else:
                low += 1
                if triplet_sum - iterable[low] in occur.keys():
                    return True
                occur[iterable[high] + iterable[low]] = [iterable[low], iterable[high]]
                occur[iterable[mid] + iterable[low]] = [iterable[low], iterable[mid]]
                current_sum += iterable[low] - iterable[low - 1]

        # If the current sum greater than triplet sum, we are decrementing index of high and modifying current sum
        else:
            high -= 1
            occur[iterable[high] + iterable[low]] = [iterable[low], iterable[high]]
            occur[iterable[high] + iterable[mid]] = [iterable[mid], iterable[high]]
            if triplet_sum - iterable[high] in occur.keys():
                return True
            current_sum += iterable[high] - iterable[high + 1]

    # If the code comes out of while loop, then no triplet sum is present
    return False
