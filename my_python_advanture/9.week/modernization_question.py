listem=[]
gir_list = [1, 2, 3]
rakam=""
for bis in gir_list:rakam+=str(bis)
for i in range(len(gir_list)):
   for j in range(len(gir_list)):
      for k in range(len(gir_list)):
         text=rakam[i]+rakam[j]+rakam[k]
         listem.append(text)
listek=[]
for gas in range(len(listem)-1):listek.append(list(listem[gas]))
final_list=[o for o in listek if o.count(rakam[0])==1 and o.count(rakam[1])==1]
print(final_list)
