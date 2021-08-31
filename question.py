num = [48, 10, 11, 21, 36, 5, 6, 52, 28, 29,
       53, 54, 45, 19, 20, 47, 55, 39, 41, 7,
       9, 17, 26, 27, 42, 22, 37, 51, 46, 18,
       44, 30, 34, 13, 15, 35, 33, 16, 50, 24]
print([i for i in range(min(num),max(num)) if i%2==0 and i not in num])


for i in [1,2,3,4,5,4,3,2,1]:
    for j in range(i):
        print("*",end=" ")
    print()


T = (1, 2, 3, 4, 5, 6, 7, 8)
print(T[T.index(5)], end = " ")
print(T[T[T[6]-3]-6])

a= {"sema1213a":"sem1240","ahem":"ahmet1234.","mehmet":"mehmet9695","salih25523":"sal4546"}




def listed(T):
    tuple_donusturuldu=[k*5 for k in T]
    return tuple_donusturuldu

print(type(listed(T)))


def fruit(*fruits):
    for i in fruits:
        print("I want to fruit:",i)

fruit("apple","orange","watermelon","vişne")

def dicc(**kywargrs):
    for keys,values in kywargrs.items():
        print(keys + " is " + values)

dicc(peter="doctor",hannah="ddentist",jacob="programmer",yavuz="master")



listek=list(range(15))

def klist(*data):
    addlist=[sum(i) for i in data]
    return addlist

print(klist(listek))




prime_list=[]
prime=int(input("please enter number"))
allnum=[p for p in range(2,prime)]
for k in allnum:
       if prime%k==0:
           prime_list.append(k)
if any(prime_list):
    print("this is not a prime number")
else:
    print("this is prime number:{}".format(prime))
















