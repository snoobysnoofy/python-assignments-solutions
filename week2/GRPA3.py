ip = input().lower()
vowels = ""

if "a" in ip:
    vowels += "a"
if "e" in ip:
    vowels += "e"
if "i" in ip:
    vowels += "i"
if "o" in ip:
    vowels += "o"
if "u" in ip:
    vowels += "u"

if vowels != "":
    print(vowels)
else:
    print('none')