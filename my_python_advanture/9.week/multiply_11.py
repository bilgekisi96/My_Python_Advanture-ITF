

n=input("lütfen sayi giriniz:")
k,listem=len(n),[]
for i in range(len(n)):
     v=k-2
     listem.append(n[v:k])
     k-=1
liste=listem[:-1]
addlist,cezve=[],0
for j in liste:
        toplam=int(j[0])+int(j[1])+cezve
        if toplam>9:
            toplam=str(toplam)
            toplam=int(toplam[1])
            cezve=1
            addlist.append(toplam)
        else:
            cezve=0
            addlist.append(toplam)
final_list=[int(n[0])+cezve]+addlist[::-1]+[int(n[len(n)-1])]
str_bagi=""
for st in final_list:str_bagi+=str(st)
print(str_bagi)
