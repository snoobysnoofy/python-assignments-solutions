def steps(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return steps(1) + steps(2) + 1
    return steps(n - 1) + steps(n - 2) + steps(n - 3)