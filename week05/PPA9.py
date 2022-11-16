# get a specific row and colummn from a matrix and return it

def get_column(mat, col):
    c = []
    for i in range(len(mat)):
        c.append(mat[i][col])
    return c

def get_row(mat, row):
    return mat[row]
