def get_range(L):
    maxi = L[0]
    for i in L:
        if i > maxi:
            maxi = i

    mini = L[0]
    for i in L:
        if i < mini:
            mini = i

    return maxi - mini