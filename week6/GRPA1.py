def get_toppers(scores_dataset, subject, gender):
    max_marks = 0
    for student in scores_dataset:
        if (student['Gender'] == gender) and (student[subject] > max_marks):
            max_marks = student[subject]

    toppers = []
    for student in scores_dataset:
        if (student['Gender'] == gender) and (student[subject] == max_marks):
            toppers.append(student["Name"])
    
    return toppers
