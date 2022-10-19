def dict_to_list(D):
    o = []
    for i in D:
        t = (i, D[i])
        o.append(t)
    
    return o
        

def list_to_dict(L):
    o = {}
    for i in L:
        o[i[0]] = i[1]

    return o