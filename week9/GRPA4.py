def num_to_words(mat):
    d = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
    f = open('output.csv', 'w')
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            f.write(d[mat[i][j]])
            if j != len(mat[i]) - 1:
                f.write(',')
        if i != len(mat) - 1:
            f.write('\n')
    f.close()