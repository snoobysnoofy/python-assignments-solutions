def get_goals(filename, country):
    f = open(filename, 'r')
    goals = 0
    players = 0
    for line in f:
        if country in line:
            goals += int(line.split(',')[2])
            players += 1
    f.close()
    if players <= 0:
        return (-1, -1)
    else:
        return (players, goals)