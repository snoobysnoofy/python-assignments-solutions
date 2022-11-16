def merge(D1, D2, priority):
    D = {}
    for key in D1:
        if key in D2:
            if priority == 'first':
                D[key] = D1[key]
            else:
                D[key] = D2[key]
        else:
            D[key] = D1[key]
    for key in D2:
        if key not in D1:
            D[key] = D2[key]
    return D