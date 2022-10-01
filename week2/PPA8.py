# start = input()
# end = input()

# files = "ABCDEFGH"

# if abs(files.index(start[0]) - files.index(end[0])) == abs(int(start[1]) - int(end[1])):
#     print("YES")
# else:
#     print("NO")

start=input()
end=input()
alpha= "ABCDEFGH"
num= "12345678"
result= "NO"
if abs(alpha.index(end[0])-alpha.index(start[0])) == abs(num.index(end[1])-num.index(start[1])):
    result= "YES"
print(result)