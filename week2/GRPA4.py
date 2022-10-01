p1 = input()
dt1 = input()
p2 = input()
dt2 = input()

d1 = int(dt1[:2])
m1 = int(dt1[3:5])
y1 = int(dt1[-4:])   

d2 = int(dt2[:2])
m2 = int(dt2[3:5])
y2 = int(dt2[-4:])

y = p1

if dt1 == dt2:
    if p1 > p2:
        y = p2

elif y1 != y2:
    if y1 < y2:
        y = p2
elif m1 != m2:
    if m1 < m2:
        y = p2
else:
    if d1 < d2:
        y = p2
        
print(y)
