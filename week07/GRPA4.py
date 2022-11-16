n = int(input())
station_dict = {}

while n > 0:
    train_name = input()
    comp = int(input())
    train_dict = {}
    for i in range(comp):
        comp, count = input().split(',')
        train_dict[comp] = int(count)
    station_dict[train_name] = train_dict
    n = n - 1
