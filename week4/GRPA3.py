n = int(input())

A = []
for i in range(n):
    A.append(list(map(int, input().split(","))))

B = []
for i in range(n):
    B.append(list(map(int, input().split(","))))

C = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(0)
    C.append(row)

for i in range(n):
    for j in range(n):
        for k in range(n):
            C[i][j] += A[i][k] * B[k][j]

        if j != n-1:
            print(C[i][j], end=",")
        else:
            print(C[i][j])