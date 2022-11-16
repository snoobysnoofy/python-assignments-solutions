def insert(L, x):
    n = []
    for i in L:
        if i < x:
            n.append(i)

    n.append(x)

    for i in L:
        if i >= x:
            n.append(i)
    
    return n