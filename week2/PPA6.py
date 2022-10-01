a = input()
l = len(a)


flag = False
if l % 2 == 0:
    if a[-1] == ".":
        a = a[:-1]
        flag = True
    else:
        a += "."
        l += 1

if l == 4 and flag == True:
    print(a)
else:
    n = (l - 3)//2
    sub_string = a[n:-n]
    print(sub_string)