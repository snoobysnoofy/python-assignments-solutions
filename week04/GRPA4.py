common=[]
a=input().split(",")
s=input().split(",")
b=[int(i) for i in s]
for i in range(len(b)):
    for j in range(i+1,len(b)):
        if b[i]==b [j]:
            s=[a[i],a[j]]
            common.append(s)
d=[]
for i in common:
    s=common.index(i)
    for j in range(len(i)-1):
        if i[j]>i[j+1]:
            u=common[s][0]
            common[s][0]=common[s][1]
            common[s][1]=u
