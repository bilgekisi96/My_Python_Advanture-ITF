
black_wall=[0,1,0,2,1,0,1,3,2,1,2,1]
liste=[]
wheather_water=[3-i for i in black_wall]
print(wheather_water)


input1='laser'
input2=['lazing', 'lazy',  'lacer']
union=[]
sayac=0
setter=[set(k) for k in input2]

while sayac<len(setter):
       if setter[sayac] == set(input1):
              if len(input2[sayac])==len(input1):
                   union.append(input2[sayac])
       sayac+=1
print(union)

alphabet=list("abcdefghijklmnopqrstuvwxyz")
alphabet_big=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
rev_alphabet=alphabet[::-1]
rev_big_alp=alphabet_big[::-1]
print(rev_alphabet)
dicc=dict(zip(alphabet+alphabet_big+list("123456789"),rev_alphabet+rev_big_alp+list("123456789")))

for i in "Christmas is the 25th of December":
       if i==" ":
           dicc[i]=" "
       print(dicc[i], end="")


kelime=["crazer","carer","racar","caers","racer"]
kelime1="racer"
liste=[]
for i in kelime:
  x =str(sorted(i))
  y =str(sorted(kelime1))
  if y  in x:
    liste.append(i)
print(liste)


black_wall=[0,1,0,2,1,0,1,3,2,1,2]
listt = []
sayac1, sayac2, total = 0, 0, 0
while True:
    answer = input("Please enter an non-negative integer or press 'q' to stop adding into the list > ")
    if answer.lower() == 'q':
        break
    else:
        listt.append(int(answer))
for x in range(max(listt)):
    listt2 = []
    for i in listt:
        if i != 0:
            a = listt.index(i)
            break
    for k in listt[::-1]:
        if k != 0:
            b = listt[::-1].index(k)
            b = len(listt) - (b + 1)
            break
    if a == b:
        break
    for v in listt[a:b]:
        sayac1 += 1
        if v != 0:
            sayac2 += 1
    total = sayac1 - sayac2
    for p in listt:
        if p == 0:
            listt2.append(p)
        else:
            p = p - 1
            listt2.append(p)
    listt = listt2
print('{} bars of water will be trapped on terrain after raining.'.format(total))

