liste=[1,2,3,4,5,6,7,8,9]
yiste=liste
asal_list=[]
for j in liste:
    for k in range(1,max(liste)+1):
        if j%k==0:
            asal_list.append(j)
asal_liste=[asal for asal in asal_list if asal_list.count(asal)==2]
asal_liste=list(set(asal_liste))
print(asal_liste)
yok_list=[yok for yok in liste if yok not in asal_liste]

print(yok_list)

if 1 in liste:liste.remove(1)
sayac,ileri=1,0
say,say_list=1,[]
for carp in liste:sayac*=carp
for i in range(len(liste)):
        while True:
            if sayac%liste[i]==0:
                sayac/=liste[i]
                ileri+=1
            else:
                say_list.append(ileri)
                ileri = 0
                break
while say_list.count(0):say_list.remove(0)
cevrim=1
print(say_list)
for c,v in list(zip(asal_liste,say_list)):cevrim*=(c**v)
print(cevrim)





















"""
lsm=lcm
bolen=[]
for k in lcm:
    for t in range(1,len(lsm)):
       if lsm[t]%k==0:
           bolen.append(k)
print(bolen)
for say in lsm:
    if bolen.count(say)>1:
        carpma/=(say**(bolen.count(say)-1))

print(carpma)
"""
