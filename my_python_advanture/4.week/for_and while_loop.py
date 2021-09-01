# for loop iterator bir object gerekiyor
#while loop ise true conditions sağladığımız sürece devameder




text="Talk is cheapp show me the code".split(" ")
sayac=0
longest=0
liste=[]
while sayac<len(text):
    if len(text[sayac])>longest:
        longest=len(text[sayac])
    sayac +=1
print(longest)
names = ["Ahmed", "Aisha", "Adam", "Joseph", "Gabriel"]
for name in names:print("hello" , name)

k=5
for j in range(11):
    print(f"{k}x{j}=",k*j)

k=0
for i in range(1,10):
    print(end="\n")
    k +=1
    for j in range(i):
        print(k,end=" ")


text="clarusway"
sayac=0
for i in text:
       if sayac<len(text)-1:
            i=i+"-"
            sayac+=1
       print(i,end="")


ls = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
n = 0
a = 0
b = 1
while ls.count(max(ls)) == 1:
    ls[ls.index(max(ls))]-=1
while b < len(ls):
    if ls[a] > ls[b]:
        while ls[a] > ls[b]:
            if ls[a] not in ls[b:]:
                break
            else:
                n+=ls[a]-ls[b]
                b+=1
                if b == len(ls):
                    break
        a = b
        b = a+1
    else:
        a+=1
        b+=1
print(n)






