def is_empty(L):
    if len(L) == 0:
        return True
    else:
        return False
    
def first(L):
    if is_empty(L):
        return "None"
    else:
        return L[0]

def last(L):
    if is_empty(L):
        return "None"
    else:
        return L[-1]

def init(L):
    if is_empty(L):
        return "None"
    elif len(L) == 1:
        return []
    else:
        return L[:-1]

def rest(L):
    if is_empty(L):
        return "None"
    elif len(L) == 1:
        return []
    else:
        return L[1:]