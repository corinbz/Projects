from itertools import product
from timeit import default_timer as timer

start = timer()
lst = [str(i) for i in range(0, 10)]


def finder(n):
    numbers = []
    counter = 0
    n_digits = 2
    while n > counter:
        print('n =', n,'   counter =', counter)
        tot_perm = list(product(lst, repeat=n_digits))

        for perm in tot_perm:
            a = ''
            for number in perm:
                a += number
            b = a[::-1]
            if a == b or a[0] == '0' or b[0] == '0':
                continue

            b = int(a[::-1])
            a = int(a)

            # if a > (int('9'*n_digits)+5)/2:
            #     break

            add = a+b
            minus = abs(b - a)

            if add % minus == 0 and a not in numbers:
                numbers.append(a)
                numbers.append(b)
                # counter = len(numbers)
        counter = len(numbers)

        n_digits += 1
        print('n_digits =', n_digits, '\n')

    return numbers, len(numbers)


def sum_dif_rev(n):
    return numbers_lst[n-1]


numbers_lst, counter = finder(65)
print(sorted(numbers_lst), counter)
print(sum_dif_rev(3))

end = timer()
print('time =', end - start, 's')
