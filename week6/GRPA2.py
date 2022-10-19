def counter(words):
    count = {}
    for i in words:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count

def freq_to_words(words):
    count = counter(words)
    freq = {}
    for i in count:
        if count[i] in freq:
            freq[count[i]].append(i)
        else:
            freq[count[i]] = [i]

    return freq