score_dict = {}
for i in range(8):
    l = input().split(",")
    score_dict[l[0]] = len(l) - 1

sorted = []
while score_dict:
    max_score = -1
    for team, score in score_dict.items():
        if score > max_score:
            max_score = score
            max_team = team
        elif score == max_score and team < max_team:
            max_team = team

    score_dict.pop(max_team)
    print(f"{max_team}:{max_score}")
