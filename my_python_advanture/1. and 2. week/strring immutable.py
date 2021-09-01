


metin="clarusway"
print(f"{metin.capitalize()}")

metin1="perceptron"

print(f"{metin1.title()}")   #  f stringin içerisine işlem uygulayabiliriz



#STRİNGİN İMMUTABLE DEĞİŞTİRİLEMEZ ÖZELLİĞİ

a="yavuz"
a.capitalize() #  bu stringi değiştirmez
b=a.capitalize() # ama bir değişkene atarsak o zaman değişir yada direk kendisine atarsak
print(b)

text="www.yavuzselimozkok.com"

print(text.startswith("w")) # bu direk true döndürür
print(text.endswith("com")) # buda döndürür true çünkü ikiside sorguluyor

#  Bu ifadelere method deniyor yani bir veri üzerine uygulandığında bir metot oluşturmuş oluyoruz
#

text1="S0d0me and G0m0re"

text1=text1.replace("0","o")
text1.replace("0","o",2) #  ilk 2 tane 0 ı o yapar gerisine dokunmaz
print(text1)

source_string="interoperability"

source_string=source_string.strip("iy") #  baştan ve sondan tüm boşlukları eğer içine karakter girersek onlarıda temizler

print(source_string)

word="clarusway"

sentence="haypatia"

listek=[sentence]
print(listek)
print(list(sentence))

number=float(input("please enter numbr"))

print(f"${number:.2f}")           #  string üzerinde float değerin ilk 2 değerini gösterebiliyoruz f stringte

print("${:.2f}".format(number))   #  aynısı format metodu ilede geçerli tabikide :)







