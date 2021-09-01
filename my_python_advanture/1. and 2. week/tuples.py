empty_list=[]
empty_list.append(6666)
empty_list.append("multiverse")
empty_list.append([0])

print(empty_list)


tuple1=tuple(range(1,11))
tuple2=tuple(range(1,8))
a,b,c=0,1,2
print(len(tuple1))
while a<len(tuple1):
     print( "{} x {}={}".format(tuple1[a],b,tuple1[a]*b))
     a = a + 1
a=0
while a<len(tuple2):
     print( "{} x {}={}".format(tuple1[a],c,tuple1[a]*c))
     a = a + 1


my_listst=[1,2,5,4,2,4,1,2,5,6,2,44,2,5,5,5,5]
my_count=[my_listst.count(cnt) for cnt in my_listst]
print(my_listst[my_count.index(max(my_count))])

listw = list(range(12))
listw_kare = []
sayi=0
while sayi<12:
     kare=listw[sayi]**2
     listw_kare.append(kare)
     sayi=sayi+1
     if sayi==12:
          print(listw_kare)









