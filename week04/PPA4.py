L = input().split(',')

maxlen = ""
for i in L:
    if len(i) >= len(maxlen):
        maxlen = i
print(maxlen)