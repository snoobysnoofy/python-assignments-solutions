names = input().split(",")
days = input().split(",")
common = []

l = len(names)
for i in range(l):
    for j in range(i+1, l):
        if i != j and days[i] == days[j] and names[i] < names[j]:
            p = [names[i], names[j]]
            common.append(p)