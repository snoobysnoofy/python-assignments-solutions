def linear(P, Q, k):
    if (len(P) != len(Q)):
        return False
    if P == []:
        return True
    if P[0] == k * Q[0]:
        return linear(P[1:], Q[1:], k)
    else:
        return False