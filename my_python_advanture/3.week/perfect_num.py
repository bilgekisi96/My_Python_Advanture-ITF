



muq=int(input("please enter muq num"))
listem=[]
muq_num=[]
for i in range(1,muq):
    for j in range(1,i):
        if i%j==0:
          listem.append(j)
          if sum(listem)==i:
              muq_num.append(i)
    listem=[]
print(muq_num)













