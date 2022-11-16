n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split(" "))))

s = int(input())
for i in range(n):
    for j in range(n):
        matrix[i][j] *= s

        if j < (n-1):
            print(matrix[i][j], end=" ")
        else:
            print(matrix[i][j])