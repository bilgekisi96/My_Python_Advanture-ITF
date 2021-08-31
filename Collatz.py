



def collatznums(n):
    collist=[]
    while n>1:
        if n%2==0:
            n /= 2
            collist.append(n)
        else:
            n=3*n+1
            collist.append(n)
    return collist
print(collatznums(13))
