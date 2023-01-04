def tail_recursive_sum(n, acc=0):
    if n == 0:
        return acc
    return tail_recursive_sum(n - 1, acc + n)

print(tail_recursive_sum(5))