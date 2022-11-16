a = input()

smallest = a
while a != "abcdefghijklmnopqrstuvwxyz":
    if len(a) < len(smallest):
        smallest = a
    a = input()

print(smallest)