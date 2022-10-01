a = float(input())

if a < 0:
    if int(a) != a:
        print(int(a-1))
    else:
        print(int(a))
    print(int(a))

else:
    print(int(a))

    if int(a) != a:
        print(int(a+1))
    else:
        print(int(a))