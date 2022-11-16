def rotate(mat):
    rn = len(mat)
    cn = len(mat[0])
    rmat = []

    for j in range(cn):
        col = []
        for i  in range(rn - 1, -1, -1):
            col.append(mat[i][j])
        rmat.append(col)

    return rmat