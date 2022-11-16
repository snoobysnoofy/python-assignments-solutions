a = input()

flag = True

if int(a[0]) <= 5 or len(a) < 10:
    flag = False
for i in range(0, len(a)):
    if a.count(a[i]) > 7 or (a[i]*6 in a):
        flag = False
if flag:
    print('valid')
else:
    print('invalid')