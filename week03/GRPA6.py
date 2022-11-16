n = int(input())

for i in range(1, n+1):
    for j in range(1, i):
        print(j, end=",")
    print(i)
for i in range(n-1,0,-1):
    for j in range(1,i):
        print(j, end=",")
    print(i)
