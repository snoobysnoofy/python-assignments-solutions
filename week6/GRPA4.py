def two_level_sort(scores):
    sorted = []
    while scores:
        mini = scores[0]
        for i in range (len(scores)):
            if scores[i][1] < mini[1]:
                mini = scores[i]

            elif scores[i][1] == mini[1]:
                if scores[i][0] < mini[0]:
                    mini = scores[i]    

        sorted.append(mini)
        scores.remove(mini)

    return sorted