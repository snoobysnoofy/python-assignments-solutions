n = int(input())
s = []
d = []
for i in range(n):
    s.append(list((map(int, input().split(",")))))

p = list(map(int, input().split(",")))
x2 = p[0]
y2 = p[1]

for i in s:    
    x1 = i[0]
    y1 = i[1]

    distance = (((x1 - x2)**2) + ((y1 - y2)**2))**(1/2)
    d.append(distance)

l = len(s)

min = 1001
for i in range(l):
    if d[i] < min:
        min = d[i]
        index = i

for i in range(l):
    if d[i] == min:
        for j in range(2):
            if j != 1:
                print(s[i][j], end=",")
            else:
                print(s[i][j])