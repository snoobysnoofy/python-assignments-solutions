n = int(input())

if n > 5:
    for i in range(1,n):
        for j in range(1,n):
            for k in range(1,n):
                if i**2 + j**2 == k**2 and i < j < k:
                    print(i, j, k, sep=",")
                    break
else:
    print("NO SOLUTION")