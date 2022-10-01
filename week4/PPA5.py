L = input().split(" ")

for i in range(len(L)):
    if float(L[i]) > 0:
        L[i] = int(float((L[i])))
    else:
        L[i] = int(L[i]-1)

for i in range(len(L)):
    if i != len(L)-1:
        print(L[i], end = ",")
    else:
        print(L[i])
