def strlovers(user):
    cift="loves me not"
    tek="loves me"
    strlist=[]
    liste=[i for i in range(1,user+1)]
    for sf in liste:
        if sf%2==0:
            strlist.append(cift)
        else:
            strlist.append(tek)
    strlist[len(strlist)-1]=strlist[len(strlist)-1].upper()
    return strlist
print(strlovers(5))
print(strlovers(1))












