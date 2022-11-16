def first_three(L):
    for i in range(len(L)):
        for j in range(i, len(L)):
            if L[j] > L[i]:
                L[i], L[j] = L[j], L[i]
    
    return L[0], L[1], L[2]


##### different approach

def first_three1(L):
    fmax, smax, tmax = L[0], L[1], L[2]
    
    for i in L:
        if i > fmax:
            tmax = smax
            smax = fmax
            fmax = i
        elif i > smax and i < fmax:
            tmax = smax
            smax = i
        elif i > tmax and i < smax:
            tmax = i

    return fmax, smax, tmax