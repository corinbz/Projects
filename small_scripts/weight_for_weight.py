import collections


def order_weight(strng):
    new_dict = {}
    for i, e in enumerate(strng.split()):
        a = list(e)
        new_dict[i] = (sum(int(x) for x in a))

    ordered_dict = collections.OrderedDict(sorted(new_dict.items(), key=lambda t: t[1]))
    print(ordered_dict)

    for i in iter(set(ordered_dict.values())):
        if list(ordered_dict.values()).count(i) > 1:



print(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"))
