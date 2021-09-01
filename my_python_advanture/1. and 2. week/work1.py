
"""
celcius = int(input("Lütfen sıcaklık değerini celcius cinsinden giriniz:\n"))
fahrnyt = ((celcius)*1.8)+32
print("işte fahrenayt geliyor {} celcius: {}F dir\n\n".format(celcius,fahrnyt))


#  1 kilometre 0,621371192 mil ediyor

one_mile=0.62137119
kilo_mtre=int(input("Lütfen bir kilometre cinsinden bir değer giriniz\n"))
mil=(kilo_mtre)*(one_mile)
print(f"İşte mil cinsinden km değeri geliyor:{mil} mil dir")

""""""
import time
list=[2,3,4,5,6,5,4,3,2]
n=0
for i in range(1,10):
   for j in range(1,8):
      print("*",end=" ")
      time.sleep(0.3)
   time.sleep(0.2)
   print("")
   for k in range(1,list[n]):
     print("",end=" ")
   n=n+1
print("Clarusway")
"""

"""
import os
os.getcwd()
a=[1,2,3,4,5,8,9]
g=[1,2,3,4,5,8,9,10]




liste=["string",4,3.5,True]


b,c,d,e = "aslan",True,45,38.5


degisken="%43^+&/(!'^"

degisken2="ali hasan"

text = " ali okula gitti okuldan dönerken eve uğradı daha sonra yattı "

text2=" osman yurda gitti "

#len fonksiyonu yanlızca iterable ifadelerde çalışmaktadır



liste2=["ali","hasan",11,10.5]









"""
"""
celsius=int(input("hava sıcaklığını giriniz : \n"))

Fahrenayt=(celsius*1.8)

Kelvin=(celsius-273)

print(f"bu deger fahrenayt degeridir:{Fahrenayt}\n")

print("bu deger kelvin {}  Fahrenayt {} degeridir".format(Kelvin,Fahrenayt))

"""
"""
step=10

step2=20

"step"

"step2"

step += step
print(step)

#eşit eşittir eşit ifadesine eşit anlamını taşır ama = ifadesi eşittir ifadesini taşımaz

" > , < , =< , >= , == "

liste5=[1,2,5,6,8,9]

liste6=[1,2,5,6,8,9,10]

#Estimating the risk of death from coronavirus

#Are you a cigarette addict older than 75 years old? Variable → age

#Do you have a severe chronic disease? Variable → chronic

#Is your immune system too weak? Variable → immune


print("enter your answers with 1 or 0\n")

age=int(input("Are you a cigarette addict older than 75 years old?\n"))
chronic=int(input("Do you have a severe chronic disease? \n"))
immune=int(input("Is your immune system too weak? \n"))


dead=(not age and not chronic and not immune)


print(f"bu adamın yaşama ihtimali varmı {dead}")

"""



#number=int(input("please enter a number"))

#leap=((number%4==0) and (number%400==0 and number%100==0))
#print(leap)

list_5=[[-1,10],[8,50],[-4,40]]
list_5.sort()

print(list_5)

print([1,5,6,8][2])

print(sorted(range(11),reverse=True))

print([x for x in range(11)][::-1])

print([list(range(1,11))][0][::2])


word = 'clarusway'
n = 3
front = word.replace("r","")

print(front)

sozluk=dict(planet="world",place="turkey",school="yasar university",status="engineer",)

bakteri = {"direnc_bakterisi":"stafico",
           "termofilyus":"ısıya_dayanıklı",
           "ecoli":"dna_technologies",
           "pinus":"cam_agacı",
           'number': 40 }



print("direnc_bakterisi" in bakteri)
print(bakteri.items())
for i,j in bakteri.items():
    print("{} = {}".format(i,j))

print(bakteri.keys(),"\n")
print(bakteri.values(),"\n")
print(bakteri["number"])

liste1=[1,2,5,4,7,8,5]
liste2=[10,9,5,7,3,5,7]
a=set(liste1)
b=set(liste2)
print(a.difference(b))
print(a.union(b))
c=a.intersection(b)
c=list(c)
print(c)


fruits_vegetables = ["fruit", "vegetable", ["apple", "banana", ["mango", "avocado"]], ["spinach", "broccoli"]]

































