

"""
#map ve filter fonksiyonu

print(list(map(lambda x:x if x%2==0 else 0,[1,2,3,4,5,6,7,8,9])))


def trapple(n):
    return lambda x:n(x)
coolkarma = trapple(print)
turkissh_max=trapple(max)
toplam=trapple(sum)

coolkarma(toplam([1,2,3,4,5]))

"""



#coolkarma("seni seviyorum")
#coolkarma("hello world")
#coolkarma("merhaba dünya")

#print(turkissh_max([1,2,3,4,5,6,7,8,9]))
#coolkarma(toplam({1,2,3,4,5,6}))

"""
shiftToLeft(5, 2) ➞ 20

shiftToLeft(10, 3) ➞ 80

shiftToLeft(-32, 2) ➞ -128

shiftToLeft(-6, 5) ➞ -192

shiftToLeft(12, 4) ➞ 192

shiftToLeft(46, 6) ➞ 2944
"""

#print((lambda a,b:a*(2**b))(4,6))


liste=[]
k=int(input("sayi giriniz:"))

print(list(range(5)))
for n in range(1,k+1):
  liste.append(sum(range(n+1)))
print(liste)
print(sum(liste))


#collaction types lar iterabledır
print("yavuz"+"trapple")

a="hasan"
for i in "recep":
    a=a+i
print(a)

print([1,2,3]+[5,6,8])
