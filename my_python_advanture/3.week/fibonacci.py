#0, 1, 1, 2, 3, 5, 8, 13, 21


liste = [0,1]
a,b=0,1
while a<48:
    toplam=liste[a] + liste[b]
    liste.insert(b+1,toplam)
    a += 1
    b += 1
print(liste)
print(len(liste))


sentence="The quick Brow FFox"
sentence=sentence.replace(" ","")
lisbig=[]
[lisbig.append(g) for g in sentence if g.count(g.upper())]
kucuk,buyuk=len(sentence)-len(lisbig),len(lisbig)
print("Buyuk harf karakter sayisi:{}".format(buyuk))
print("Kucuk harf karakter sayisi:{}".format(kucuk))



