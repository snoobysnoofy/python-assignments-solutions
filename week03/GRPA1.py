n = int(input())

sum = 0
rsum = 0
for i in range(1, n+1):
    sum = 0
    for j in range(1, i+1):
        sum += j
    rsum += sum

print(rsum)