def solution(marks):
    for i in range(len(marks)):
        for j in range(i + 1, len(marks)):
            if marks[j] < marks[i]:
                marks[i], marks[j] = marks[j], marks[i]
    
    l = len(marks)
    if len(marks) % 2 == 0:
        median = (marks[l//2-1] + marks[l//2]) / 2
    else:
        median = marks[l//2]

    return median

marks = [100,99,98,97,96,95,10,11,12,13,14,15,16,17]
print(solution(marks))