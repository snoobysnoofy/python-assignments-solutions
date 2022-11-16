def get_marks(scores_dataset, subject):
    o = []
    for studends in scores_dataset:
        o.append((studends["Name"], studends[subject]))
    
    return o