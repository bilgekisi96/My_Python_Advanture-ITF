

import os
import shutil
dosya=os.listdir()
print(dosya)
#shutil.make_archive()#zipliyor

#read readlines wwrite writelines
#open() function için open(file,mode okumamı yazmamı yapıcam
#encoding=uicode Transformation Format
#open()#file name and path
#open fonksiyonun içine en uygun unicodu yazıcazdefault mode reading
#için ayarlanmış durumda
#bir tane dosymız var my_file=open("first_file.txt")
#print(type(my_file))#textwrapper olarak geçiyor
#.txt.cvs .tsv .md .xml .json dosyaları

file=open("fishes.txt","r")
print(file.read())
file.close()

#read içine bir rakam girdiğimizde ne yapar sadece 33 karakterlik kısmını veriyor
print()

file=open("fishes.txt","r")
content = file.read()#bir değişkene atayabiliriz
file.close()
print(len(content))


file=open("fishes.txt","r")
print(file.read(33))
print(file.tell())
file.seek(0) #courseri oraya taşır
print(file.read(33))
print(file.tell())#courserin nerede kaldığını bize söylüyor

#file objectinin üzerine bu metodları uyguladık read writeline
print()

rumi=open("rumi.txt","r")

part_1=rumi.readline()
part_2=rumi.readline(21)
part_3=rumi.readline(18)
print(part_1)
print(part_2)
print(part_3)
print(rumi.tell())
rumi.close()
#readlineslara devam edicez








