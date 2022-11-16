pword = input()
nl = ["/", "\\", "=", "'", '"', " "]
pl = list(pword)

is_valid = True

if (pl[0].isalpha() != True):
    is_valid = False

if (len(pl)) < 8 or (len(pl) >= 32):
    is_valid = False
    
for i in pl:
    if i in nl:
        is_valid = False

print(is_valid)
