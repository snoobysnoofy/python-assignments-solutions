import string

s = input().lower()
t = string.ascii_lowercase
o = ""
for i in t:
    for j in s:
        if i == j:
            o += j
print(o)