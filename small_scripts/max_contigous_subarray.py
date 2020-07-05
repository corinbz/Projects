def max_cont_sub(arr):
    max_so_far, max_ending_here = 0, 0
    for item in arr:
        max_ending_here += item
        if max_ending_here < 0:
            max_ending_here = 0
        elif max_so_far < max_ending_here:
            max_so_far = max_ending_here
    return max_so_far


print(max_cont_sub([7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]))
