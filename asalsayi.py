

sayi=int(input("lutfen sayiyi giriniz"))
asalclass=[]
asalmi=True

if sayi==1:
    asalmi=False

for i in range(2,sayi):
    if sayi%i==0:
        asalmi=False
        break

if asalmi:
    print("sayi asaldır")
else:
    print("sayi asal degildir")
