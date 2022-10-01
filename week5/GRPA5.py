# returns transpose of a matrix

def transpose(mat):
    rn = len(mat)
    cn = len(mat[0])
    tmat = []
    for i in range(cn):
        col = []
        for j in range(rn):
            col.append(mat[j][i])
        tmat.append(col)
    return tmat







mat = [1, 2, 3, 4, 5]



print(transpose(mat))