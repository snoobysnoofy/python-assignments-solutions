num = (input())

L = num.split(",")
max = -1
for i in L:
    if int(i) > max:
        max = int(i)
print(max)