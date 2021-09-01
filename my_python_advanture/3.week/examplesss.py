




alphabet=("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","x","w","y","z")
tup=[i for i in range(1,len(alphabet)+1)]
dicc=dict(list(zip(alphabet,tup)))
sent=input("please enter your string").lower().split(" ")
print(sent)
numbers=[]
toplam,sayac=0,0
while sayac<len(sent):
    for k in sent[sayac]:
        toplam += dicc[k]
    numbers.append(toplam)
    sayac +=1
    toplam=0
print(numbers)
print(sent[numbers.index(max(numbers))])
