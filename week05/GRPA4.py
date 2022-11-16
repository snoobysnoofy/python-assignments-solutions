## check if a matrix is a magic square

# get sum of all the rows
# and columns of a matrix
# and diagonals too
# and check if they are equal

def is_magic(mat):
    l = len(mat)
    dsum1, dsum2 = 0, 0
    for i in range(l):
        dsum1 += mat[i][i]
        dsum2 += mat[l - 1 - i][i]

    if dsum1 != dsum2:
        return "NO"

    
    for i in range(l):
        rsum, csum = 0, 0
        for j in range(l):
            rsum += mat[i][j]
            csum += mat[j][i]
        if rsum != csum:
            return "NO"

    return "YES"
