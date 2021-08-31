


"""
baslangic=int(input("enter num for begin"))
bitis=int(input("enter num for finish"))
if baslangic>bitis:print("this is mistake for entry")
else:print(sum([i for i in range(baslangic+1,bitis)]))
print()

def largest(args):
    list1 = []
    for i in range(args):
        num = int(input("please enter number : "))
        list1.append(num)
    list2 = sorted(list1,reverse=True)
    return list2[0]
print(largest(2))
"""

print(set("aet")==set("eat"))
a=[i*2 for i in range(10)]
print(a)
print("a"+"n"+"t")


listem=["ali","hasan","mehmet","kamil","gamze","efsa"]
my_dicc={}
my_dicc=my_dicc.fromkeys(listem,[])
print(my_dicc)

squre_dicc={}


for x in range(10):
    squre_dicc[x]=x*x



def identfy(*kup):
    kup=list(kup)
    sayac=0
    for i in kup:
        sayac+=1
    if sayac==3:
        toplam=0
        for j in kup:
             toplam+=len(j)
        if toplam==9:
            print("full")
        else:print("missing values")
    else:print("non full")

identfy(["O", "O", "O"],["O", "O", "O"],["0","0","0"])

for x in [1,2,3,4]:print((lambda x:"odd" if x%2!=0 else "even")(x))



liette1=["o","s","t","t"]
letter2=["n","i","e","w"]
letter3=["e","x","n","o"]
result=map(lambda x,y,z:x+y+z,liette1,letter2,letter3)
print(list(result))


num1=[1,2,3,4]
num2=[3,2,1,0]
result_num=map(lambda t,v:(t+v)/2,num2,num1)
print(list(result_num))


kelimeler = ["ali veli deli", "mehmet ağanın kuzeni", "cemilin-bacısı"]
result_map=map(lambda x:len(x),kelimeler)
print(list(result_map))


words = ["apple", "swim", "clock", "me", "kiwi", "banana"]

print(list(filter(lambda x:len(x)>=5,words)))

wowls=["a","e","o","ö","u","ü","i","ı"]

first_ten=["a","b","c","d","e","f","g","h","i","j","k","l"]
print(list(filter(lambda x:x in wowls,first_ten)))