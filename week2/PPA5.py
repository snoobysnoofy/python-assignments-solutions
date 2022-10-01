x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())


if x1 == x2:
    print("Vertical Line")
else:
    slope = (y2-y1)/(x2-x1)
    y3 = y1 + slope*(x3-x1)
    print(y3)

    if slope > 0:
        print("Positive Slope") 
    elif slope < 0:
        print("Negative Slope")
    else:
        print("Horizontal Line")