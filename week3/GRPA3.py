a = input()

sp = [0, 0]

while a != "STOP":
    a = input()
    if a == "UP":
        sp[0] += 1
    if a == "DOWN":
        sp[0] -= 1
    if a == "LEFT":
        sp[1] -= 1
    if a == "RIGHT":
        sp[1] += 1  

d = abs(sp[0]) + abs(sp[1])
print(d)