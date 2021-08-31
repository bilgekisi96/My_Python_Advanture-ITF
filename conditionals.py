# if statements conditionlar ile çalışır
# None [] () "" 0 {} bu ifadeler falsy
# boş liste tuple sözlük string
# boş collection ve iterablellar

# case ve intendation sensitive
#compration operatorlardan sonra alacağımız değer true
# false olur

#if set("TWELVE PLUS ONE")==set("ELEVEN PLUS TWO"):
 #   print("we are same")

#user=input("enter answer yes or no").title().strip() == "Yes"

#print("you entered",user)

#if contion:
   #execute body
#else:
   #execute body
#else için tüm olasılıklar geçerli oluyor

sayac=0
lisdir=[1,2,5,9,6,3,2,5,2,2,9,2]
listder=[]
while sayac<len(lisdir):
    eleman_sayisi=lisdir.count(lisdir[sayac])
    sayac += 1
    listder.append(eleman_sayisi)

most_frequent=lisdir[listder.index(max(listder))]
times=lisdir.count(most_frequent)
print(f"the most frequent number is {most_frequent} and it was {times} times repeated")




farm = ["eat","tea", "tan", "ate", "nat", "baT","peek","keep"]
farmharvest = []
farmharve=[]
farmlow=[low.lower() for low in farm]
farmsetter=set(farmlow)
farmset=[set(x) for x in farmsetter]
print(farmset)
baslangic=0




"""
farmsetcount=[farmset.count(coun) for coun in farmset]
print(farmsetcount)
farmcountlist=list(set(farmsetcount))
farmconc=list(zip(farmlow,farmsetcount))
farmconc=dict(farmconc)

for j in range(4):
 for sec in farmlow:
    if farmconc[sec]==farmcountlist[j]:
       farmharvest.append(sec)
 farmharve.insert(j,farmharvest[:])

print(farmharve)
"""

"""
num1=int(input("enter number"))
num2=int(input("enter number"))
nu3=int(input("enter number"))
if num1>num2 and num1>nu3:
    print("num1 is greater")
elif num2>nu3 and num2>num1:
    print("num2")
else:
    print("num3")
"""


# if elif else bloklarından herhangi birisi true döndürür ise altındaki bloklardan biri de
# devreye girer çalışır ve çıkar


student=int(input("enter not"))
if student>0:
    if student>79 and student<=84:
         print("B")
    if student>84 and student<=90:
        print("B+")
    elif student>90 and student<=95:
        print("A")
    elif student>95:
        print("A+")
else:
    print("below B")

items = (10,20) #tuple için parantese gerek yok
x,y=items  #unpucking x=10 y=20 oldu

a, _, b,_ = (10,20,30,40) #place holder
print(a,b,_) # dersek 40 ı alır enson hangisiyse onu alır hata vermez hafızadan kar ederiz

x,y,*z=(11,22,33,44,55) #ilk ikisini almak istiyorum geri kalanı ayrı bir değişkende toplamak istiyoruz
print(z) #hepsini z de topladı
x,y,*_=(11,22,33,44,55,66,77) #böyle yaparsak sadece x ve y yi almış olduk

x,y,*z,t = (11,22,33,44,55,66,77) #ilk ikiyi x ve y ye atıcaz 77 yi t ye atıcaz aradakileri z ye atıcaz
print(z)

seq=[1,1,1,1,2,3,4,5,5,5,6,66,8,8]
print(max(seq,key=seq.count)) # en çok tekrar eden değeri key parametresine göre her elemanını sayacak en çok tekrar edenini
# max olarak bulmaktadır max iterablın elemanşarından birini döndürecek
# neye göre max seçeceğini

left = {"q", "w", "e", "r", "t", "a", "s", "d", "f", "g", "z", "x", "c", "v", "b"}
right = {"y", "u", "i", "o", "p", "h", "j", "k", "l", "n", "m"}
word = "test"

set_word=set(word)

print(set_word-right)