def reverse(L):
    if len(L) == 0:
        return []
    else:
        return reverse(L[1:]) + [L[0]]