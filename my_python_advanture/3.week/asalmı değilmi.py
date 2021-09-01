prime_list=[]
prime=int(input("lütfen bir sayi girniz"))
allnum=[p for p in range(2,prime)]
for k in allnum:
       if prime%k==0:
           prime_list.append(k)
if any(prime_list):
    print("bu bir asal sayi değildir")
else:
    print("bu bir asal sayidir:{}".format(prime))