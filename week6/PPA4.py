def value_to_keys(D, value):
    o = []
    for i in D:
        if D[i] == value:
            o.append(i)

    return o
