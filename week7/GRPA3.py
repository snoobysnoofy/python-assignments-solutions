def minor_matrix(M, i, j):
    l = len(M)

    minor_mat = []
    for row in range(l):
        if row != i:
            minor_row = []
            for col in range(l):
                if col != j:
                    minor_row.append(M[row][col])
            minor_mat.append(minor_row)
    return minor_mat