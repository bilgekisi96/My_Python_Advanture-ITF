



user=int(input("enter your detector:"))

sayac=0
while 0<user:
    user_inputs=int(input("enter your numbers"))
    if user_inputs>sayac:
        sayac=user_inputs
    user -= 1

print(sayac)


user=int(input("enter your detector:"))
if user>0:
    listem=[]
    for i in range(user):
        num=int(input("enter your numbers"))
        listem.append(num)
    tekli=sorted(listem,reverse=True)
    print(tekli[0])
else:
    print("enter positeve number ")












