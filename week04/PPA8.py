n = int(input())

for i in range(n):
    for j in range(n):
        if i == j:
            if j == n-1:
                print(1, end="")
            else:
                print(1, end=",")
        else:
            if j == n-1:
                print(0, end="")
            else:
                print(0, end=",")
    print()