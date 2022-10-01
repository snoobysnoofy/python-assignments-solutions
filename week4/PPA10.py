n = int(input())

def make_matrix(n):
    m = []
    for i in range(n):
        m.append(list(map(int, input().split(","))))
    return m

A = make_matrix(n)
B = make_matrix(n)

for i in range(n):
    for j in range(n):
        if j < (n-1):
            print(A[i][j] + B[i][j], end=",")
        else:
            print(A[i][j] + B[i][j])