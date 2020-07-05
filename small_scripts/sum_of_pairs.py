import random
import timeit

l1 = [1, 4, 8, 7, 3, 15]
l2 = [1, -2, 3, 0, -6, 1]
l3 = [20, -13, 40]
l4 = [1, 2, 3, 4, 1, 0]
l5 = [10, 5, 2, 3, 7, 5]
l6 = [4, -2, 3, 3, 4]
l7 = [0, 2, 0]
l8 = [5, 9, 13, -3]


# l9 = [random.randint(-100, 100) for _ in range(100000000)]


def sum_pairs2(arr, num):
    elem = (0, 0)
    for i, v in enumerate(arr):
        for j, w in enumerate(arr):
            if v + w == num and i != j and sorted(elem) != sorted([v, w]):
                del arr[j + 1:]
                elem = [v, w]
    return elem


def findPair(A, sum):
    # create an empty Hash Map
    dict = {}

    # do for each element
    for i, e in enumerate(A):

        # check if pair (e, sum-e) exists

        # if difference is seen before, print the pair
        if sum - e in dict:
            # # print("Pair found at index", dict.get(sum - e), "and", i)
            # print(f" sum - e is {sum - e}\n e is {e}")
            # print(f" dict.get(sum-e) is {dict.get(sum-e)}\n i is {i}")
            return [sum - e, e]

        # store index of current element in the dictionary
        dict[e] = i

    # No pair with given sum exists in the list
    return None


findPair([10, 5, 2, 3, 7, 5], 10)


def sum_pairs(lst, s):
    cache = set()
    for i in lst:
        if s - i in cache:
            return [s - i, i]
        cache.add(i)


# starttime = timeit.default_timer()
# print("The start time is :", starttime)
# print(sum_pairs2(l9, 129))
# print("The time difference is :", timeit.default_timer() - starttime)


print(timeit.timeit("""def findPair(A, sum):
    # create an empty Hash Map
    dict = {}

    # do for each element
    for i, e in enumerate(A):

        # check if pair (e, sum-e) exists

        # if difference is seen before, print the pair
        if sum - e in dict:
            # # print("Pair found at index", dict.get(sum - e), "and", i)
            # print(f" sum - e is {sum - e}\n e is {e}")
            # print(f" dict.get(sum-e) is {dict.get(sum-e)}\n i is {i}")
            return [sum - e, e]

        # store index of current element in the dictionary
        dict[e] = i

    # No pair with given sum exists in the list
    return None


findPair([10, 5, 2, 3, 7, 5], 10)""", number=1000000))
