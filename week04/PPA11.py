def solution(L):
    sorted_L = []

    while len(L) != 0:
        maxi = L[0]
        for i in L:
            if i > maxi:
                maxi = i

        sorted_L.append(maxi)
        L.remove(maxi)
        return sorted_L