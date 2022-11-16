a = input().split(" ")
b = input()
c = 0

flag = False
for i in a:
    if i == b:
        c += 1
        flag = True
if flag:
    print("YES")
    print(c)
else:
    print("NO")
