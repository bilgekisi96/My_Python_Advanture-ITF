
user=int(input("binary etmek istediğiniz sayiyi giriniz:"))
sayac=0
if user==0:
    print(000000)
else:
    while user>=2**sayac:
        sayac+=1
    sayac -=1
    zeros=[i*0 for i in range(sayac)]
    if user-2**sayac==0:
        zeros.insert(-sayac,1)
    else:
        kalan=user-2**sayac
        upper = [2 ** k for k in range(sayac)]
        if kalan in upper:
            zeros.insert(upper.index(kalan)+1,1)
            zeros.insert(-sayac,1)
    bin=""
    for b in zeros:bin+=str(b)
    print(bin)

















