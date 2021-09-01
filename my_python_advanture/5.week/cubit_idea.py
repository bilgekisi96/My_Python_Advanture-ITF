user = int(input("please enter your num"))
if user==0:
    print([])
elif user==1:
    print([1])
elif user==2:
    print([[1],[1,1]])
else:
      z,n,y,s=0,2,1,0
      seri=[[1,2,1]]
      for i in range(user-3):
        seri.append([])
        for j in range(user-2):
            seri[y].append(sum(seri[s][z:n]))
            n+=1
            z+=1
        seri[y].insert(0,1)
        seri[y].append(1)
        y+=1
        s+=1
        z,n=0,2
      sayac=3
      print(seri)
      final=[]
      for don in seri:
        final.append(don[:sayac])
        sayac+=1
      final.insert(0,[1])
      final.insert(1,[1,1])
      print(final)


