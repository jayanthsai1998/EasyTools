
# Overall time complexity is O(n log n)

# Return True when sum of any two numbers from the iterable equals to given doublet_sum
# else returns False


def doublet_sum_occurrence(iterable, doublet_sum):

    # To check whether the given iterable is list or tuple
    if type(iterable) == list or type(iterable) == tuple:
        pass
    else:
        raise TypeError("Iterable should be of either list or tuple")

    # To check whether all the given items in the iterable are numbers only
    for item in iterable:
        if not isinstance(item, int):
            raise ValueError("Only numbers are accepted in the iterable")

    # The length of the iterable should be of minimum length 3
    if len(iterable) < 2:
        raise Exception("Length of the given iterable should be greater than 1")

    # Iterable of any type is converted to list type to perform sort operation
    iterable = list(iterable)

    # First we sort the list which takes O(n log n) time complexity
    iterable.sort()

    # Initially considering first and last elements as the doublets
    low = 0
    high = len(iterable) - 1

    current_sum = iterable[low] + iterable[high]

    # Here an element is accessed only once in the iterable
    # Hence the complexity for below loop is O(n)
    while low < high:

        # If we got the current sum is equal to the triplet sum, we are returning True
        if current_sum == doublet_sum:
            return True

        # If the current sum is less than doublet sum, we are incrementing index of low and modifying current sum
        elif current_sum < doublet_sum:
            low += 1
            current_sum += iterable[low] - iterable[low - 1]

        # If the current sum is greater than doublet sum, we are decrementing index of high and modifying current sum
        else:
            high -= 1
            current_sum += iterable[high] - iterable[high + 1]

    # If the code comes out of while loop, then no triplet sum is present
    return False