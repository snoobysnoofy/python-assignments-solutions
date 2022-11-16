n = int(input())
max = 0

while n != 0:
    if max < n:
        max = n
    n = int(input())

print(max)