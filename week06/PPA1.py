# counts the no. of times a word appears in a series of words

l = input().split(",")

freq = {}
for i in l:
    freq[i] = 0

for i in l:
    freq[i] += 1