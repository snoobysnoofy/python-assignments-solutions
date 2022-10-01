e1 = int(input())
e2 = int(input())
e3 = int(input())
e4 = int(input())
e5 = int(input())

M = "YES"
if ((e1 + e2) % 2 != 0 or
    (e2 + e3) % 2 != 0 or
    (e3 + e4) % 2 != 0 or
    (e4 + e5) % 2 != 0 or
    (e5 + e1) % 2 != 0):
    M = "NO"

print(M)