def is_key(D, key):
    return key in D


def value(D, key):
    if is_key(D, key):
        return D[key]