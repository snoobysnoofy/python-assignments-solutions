x = float(input())
y = float(input())

if x > 0 and y > 0:
    print("first")
elif x < 0 and y > 0:
    print("second")
elif x < 0 and y  < 0:
    print("third")
elif x > 0 and y  < 0:
    print("fourth")
elif x == 0 and y == 0:
    print("origin")
elif x == 0 and y != 0:
    print("y-axis")
elif x != 0 and y == 0:
    print("x-axis")