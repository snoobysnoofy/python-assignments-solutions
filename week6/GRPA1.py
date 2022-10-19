def get_toppers(scores_dataset, subject, gender):
    maxi = 0
    toppers = []
    for entries in scores_dataset:
        s_sub_marks = entries[subject]
        s_gender = entries['Gender']
        s_name = entries["Name"]
        if s_gender == gender:
            maxi = s_sub_marks

    for entries in scores_dataset:
        s_sub_marks = entries[subject]
        if s_sub_marks == maxi:
            toppers.append(entries["Name"])

    return toppers