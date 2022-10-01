n = (input())

sum = 0
for i in n:
    sum += int(i)

print(sum)

#another solution
n  = int(input())
sum = 0
while n > 9:
    ld = n % 10
    n = n // 10
    sum += ld
sum += n
print(sum)