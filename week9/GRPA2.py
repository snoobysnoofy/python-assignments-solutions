def relation(file1, file2):
    f1 = open(file1, 'r')
    f2 = open(file2, 'r')
    line1 = f1.readlines()
    line2 = f2.readlines()
    flag=True
    if line1==line2: 
        return 'Equal' 
    else: 
        for i in range(len(line1)): 
            if line1[i] not in line2[i]: 
                flag=False 
    if flag: 
        return 'Subset' 
    else:  
        return 'No Relation'