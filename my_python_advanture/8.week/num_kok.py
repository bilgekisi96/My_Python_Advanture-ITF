liste=[1,2,3,4,5,6,7,8,9,10]
listek=[]
for i in liste:
    listek.append(list(filter(lambda x:x%i==0,[1,2,3,4,5,6,7,8,9,10])))
listim=[j[0] for j in listek if len(j)==1]
vildan=[j[0] for j in listek if len(j)==1]
carpim=1
print(listek)
for k in listim:carpim*=k
print(carpim)
v=0
finlist=[]
while True:
    listim.remove(listim[v])
    belir=1
    for t in listim:belir*=t
    for h in listim:
        if belir%h==0:
            continue
        else:
            finlist.append(h)
            break
    v+=1

cirbin=1
for o in setter:cirbin*=o
print(cirbin)

