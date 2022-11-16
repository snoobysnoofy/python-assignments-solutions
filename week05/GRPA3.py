import string
a = string.ascii_lowercase

def distance(word_1, word_2):
    if len(word_1) != len(word_2):
        return - 1
    else:
        td = 0
        for i in range(len(word_1)):
            i1, i2 = a.index(word_1[i]), a.index(word_2[i])
            td += abs(i1 - i2)

        return td