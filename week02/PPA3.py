a = int(input())

if a < 0:
    print("INVALID")
elif a <= 5:
    print("NIGHT")
elif a <= 11:
    print("MORNING")
elif a <= 17:
    print("AFTERNOON")
elif a <= 23:
    print("EVENING")
else:
    print("INVALID")