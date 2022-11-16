t = int(input())
a = int(input())
b = int(input())
c = int(input())

if 0 not in [a, b, c]:
    if a + b + c == t:
        if a != b != c and a!= c:
            print("FAIR")
        else:
            print("UNFAIR")
    else:
        print("UNFAIR")
else:
    print("UNFAIR")