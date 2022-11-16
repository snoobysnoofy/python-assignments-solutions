def ancestry(P, present, past):
    if present == past:
        return [past]
    return [present] + ancestry(P, P[present], past)