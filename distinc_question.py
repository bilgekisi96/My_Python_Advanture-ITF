
listem=[]
gir_list = [1, 2, 3]
a,b,c=gir_list[0],gir_list[1],gir_list[2]
rakam=(str(a)+str(b)+str(c))
for i in [0,1,2]:
   for j in [0,1,2]:
      for k in [0,1,2]:
         text=rakam[i]+rakam[j]+rakam[k]
         listem.append(text)
listek=[]
for gas in range(len(listem)-1):listek.append(list(listem[gas]))
final_list=[o for o in listek if o.count(str(a))==1 and o.count(str(b))==1]
print(final_list)

