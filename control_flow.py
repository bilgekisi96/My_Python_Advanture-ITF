


esik_deger=10

mevcut_veri=9

text1="aliatabin"

rakam=1256532
listerakam=list(str(rakam))

listerakam1=[int(x) for x in listerakam]
print(listerakam1)

print(listerakam)

print(text1[4] == "t")

print(f"esik deger mevcut veriden büyükmü?: {esik_deger > mevcut_veri}")

print(f"esik deger mevcut veriden küçükmü: {esik_deger < mevcut_veri}")

print(f"esik deger mevcut veriye esitmi?: {esik_deger == mevcut_veri}")

print(f"esik deger mevcut veriden büyük eşitmi?: {esik_deger >= mevcut_veri}")

print(f"esik deger mevcut veriden küçük eşitmi?: {esik_deger <= mevcut_veri}")



#  if else statement için koşullar oldukça önemli bir yer tutar .
#  if koşolunu sağlamayan değerler için else kullanılır.

course="clarusway"
if course=="clarusway":
    print("you guarantied the jop")
else:
    print("think that again")

text = ['one','two','three','four','five']
numbers = [1, 2, 3, 4, 5]
for x, y in zip(text, numbers):
    print(x, ':', y)




for i in range(1,3):
    for j in range(1,11):
        print("{} x {} =".format(i,j),i*j)
        if i*j>=14:
            break









