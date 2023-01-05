def sum_recursive(lst):
    if not lst:
        return 0
    return lst[0] + sum_recursive(lst[1:])

print(sum_recursive([1, 2, 3, 4, 5]))
