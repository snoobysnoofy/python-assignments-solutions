a = input().split(",")
real_dict = {}

for word in a:
    first_letter = word[0]
    if first_letter not in real_dict:
        real_dict[first_letter] = []
        real_dict[first_letter].append(word)
    else:
        real_dict[first_letter].append(word)